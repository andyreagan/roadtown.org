# Deployment Guide

## Initial Setup (One-time)

### 1. Create the Volume
```bash
fly volumes create roadtown_data --region bos --size 3
```

### 2. Deploy
```bash
fly deploy
```

### 3. Set up Database and Admin User
```bash
# Run migrations
fly ssh console -C "python manage.py migrate"

# Create superuser
fly ssh console -C "python manage.py createsuperuser"

# Set up initial page (if needed)
fly ssh console -C "python manage.py setup_turkey_trot"
```

## Regular Updates

```bash
# Deploy new code
fly deploy

# Run any new migrations
fly ssh console -C "python manage.py migrate"
```

## Volume Details

- **Database**: `/data/db.sqlite3` (persistent)
- **Media files**: `/data/media/` (persistent)
- **Static files**: Served directly by Fly.io from `/code/static/`

## Admin Access

- **URL**: `https://roadtown.org/admin/`
- **Django Admin**: `https://roadtown.org/django-admin/`

## File Uploads

All uploaded files (PDFs, images) through Wagtail admin will be stored in the persistent volume and survive deployments.
