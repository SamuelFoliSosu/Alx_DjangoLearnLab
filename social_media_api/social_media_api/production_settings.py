# social_media_api/production_settings.py

from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'your-domain.com']

ALLOWED_HOSTS = ['your-pythonanywhere-username.pythonanywhere.com'] # Update this

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # or 'django.db.backends.postgresql'
        'NAME': 'your-db-name',
        'USER': 'your-db-user',
        'PASSWORD': 'your-db-password',
        'HOST': 'your-db-host',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Static and Media Files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# CORS Headers for API
CORS_ALLOW_ALL_ORIGINS = True # Be more specific in a real production environment