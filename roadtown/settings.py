"""
Django settings for roadtown project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['ROADTOWN_DJ_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('ROADTOWN_DJ_DEBUG', 'false').lower() in {'true', 't', 'yes'}

ALLOWED_HOSTS = ["roadtown.org", "localhost"]

# Application definition
INSTALLED_APPS = [
    # 'djangocms_admin_style',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "turkeytrot",
    # for cms, if we want it:
    # 'django.contrib.sites',
    # 'cms',
    # 'menus',
    # 'treebeard',
    # 'sekizai',
    # 'filer',
    # 'easy_thumbnails',
    # 'mptt',
    # 'djangocms_link',
    # 'djangocms_file',
    # 'djangocms_picture',
    # 'djangocms_video',
    # 'djangocms_googlemap',
    # 'djangocms_snippet',
    # 'djangocms_style',
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.locale.LocaleMiddleware', 
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = "roadtown.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [''],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # 'cms.context_processors.cms_settings',
                # 'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = "roadtown.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

# CMS_TEMPLATES = [
#     ('home.html', 'Home page template'),
# ]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# THUMBNAIL_HIGH_RESOLUTION = True
# 
# THUMBNAIL_PROCESSORS = (
#     'easy_thumbnails.processors.colorspace',
#     'easy_thumbnails.processors.autocrop',
#     'filer.thumbnail_processors.scale_and_crop_with_subject_location',
#     'easy_thumbnails.processors.filters'
# )