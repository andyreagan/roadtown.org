# roadtown.org

Django/Wagtail site for the Roadtown Turkey Trot. Hosted on a Synology NAS via Docker + Cloudflare Tunnel.

## Local Development

```bash
export ROADTOWN_DJ_SECRET_KEY=insecure
export ROADTOWN_DJ_DEBUG=true
source .venv/bin/activate
python3 manage.py runserver
```

Visit the development site at http://localhost:8000/

## Deploy to Synology

See [deploy-synology.md](deploy-synology.md) for full setup instructions.

For routine updates:

```bash
# Push code changes to Synology and rebuild
rsync -av --exclude='.venv' --exclude='.git' --exclude='db.sqlite3' --exclude='media' --exclude='.mypy_cache' --exclude='.ruff_cache' --exclude='.DS_Store' ./ synology:/volume1/docker/roadtown/
ssh synology "export PATH=/var/packages/ContainerManager/target/usr/bin:\$PATH && cd /volume1/docker/roadtown && docker compose up -d --build"

# Run any new migrations
ssh synology "export PATH=/var/packages/ContainerManager/target/usr/bin:\$PATH && cd /volume1/docker/roadtown && docker compose exec web python manage.py migrate"
```

## Save Changes

```bash
git commit -am "[description]"
git push
```
