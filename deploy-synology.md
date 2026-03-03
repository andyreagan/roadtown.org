# Deploying to Synology via Docker + Cloudflare Tunnel

## Prerequisites
- Synology NAS with Docker (Container Manager) installed
- SSH access to Synology
- Cloudflare account managing `roadtown.org`

## 1. Create a Cloudflare Tunnel

1. Go to [Cloudflare Zero Trust Dashboard](https://one.dash.cloudflare.com/)
2. Navigate to **Networks → Tunnels**
3. Click **Create a tunnel**
4. Choose **Cloudflared** connector type
5. Name it something like `roadtown-synology`
6. Copy the **tunnel token** (long string starting with `eyJ...`)
7. Add a **Public Hostname**:
   - **Domain**: `roadtown.org`
   - **Service**: `http://web:8000`
   - (This tells Cloudflare to route `roadtown.org` traffic through the tunnel to your Django container)
8. If you want `www.roadtown.org` too, add another public hostname pointing to the same service

## 2. Set Up on Synology

SSH into your Synology (or use the terminal in DSM):

```bash
# Clone the repo
cd /volume1/docker
git clone <your-repo-url> roadtown
cd roadtown

# Create .env file
cp .env.example .env
nano .env
# Fill in:
#   ROADTOWN_DJ_SECRET_KEY=<generate a new one or use your existing key>
#   CLOUDFLARE_TUNNEL_TOKEN=<paste token from step 1.6>
```

## 3. Build and Start

```bash
docker compose up -d --build
```

## 4. Initialize the Database

```bash
# Run migrations
docker compose exec web python manage.py migrate

# Create admin user
docker compose exec web python manage.py createsuperuser

# Set up initial page (if needed)
docker compose exec web python manage.py setup_turkey_trot
```

## 5. Migrate Existing Data (from Fly.io)

If you have existing data on Fly.io:

```bash
# Download the database from Fly
fly ssh console -C "cat /data/db.sqlite3" > db_backup.sqlite3

# Copy it into the Docker volume
docker compose cp db_backup.sqlite3 web:/data/db.sqlite3

# Download media files
fly ssh console -C "tar czf - /data/media" > media_backup.tar.gz
docker compose cp media_backup.tar.gz web:/tmp/media_backup.tar.gz
docker compose exec web bash -c "cd / && tar xzf /tmp/media_backup.tar.gz"

# Restart to pick up the database
docker compose restart web
```

## 6. Update Cloudflare DNS

Once the tunnel is running, go to Cloudflare DNS for `roadtown.org`:
- **Remove** any existing A/AAAA records for `roadtown.org` that point to your IP or Fly.io
- The tunnel automatically creates a CNAME record pointing to `<tunnel-id>.cfargotunnel.com`
- Cloudflare handles HTTPS termination — your app only needs to serve HTTP on port 8000

## 7. Verify

```bash
# Check containers are running
docker compose ps

# Check tunnel logs
docker compose logs cloudflared

# Check web logs
docker compose logs web
```

Visit `https://roadtown.org` — it should be live!

## Updating

```bash
cd /volume1/docker/roadtown
git pull
docker compose up -d --build
docker compose exec web python manage.py migrate
```

## Notes

- **Data persistence**: The `roadtown_data` Docker volume stores your SQLite database and media files at `/data/`. It survives container rebuilds.
- **Backups**: Consider a cron job to back up `/volume1/docker/roadtown/` and the Docker volume.
- **Tailscale**: Your existing Tailscale setup is great for SSH/admin access to the Synology itself, but isn't needed for serving the site publicly.
- **Cloudflare Tunnel vs IP mapping**: The tunnel is more secure (no inbound ports) and works even if your ISP changes your IP.
