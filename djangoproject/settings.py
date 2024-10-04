"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import time
import os
import psycopg2
from django.db.utils import OperationalError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'user_auth.User'

JWT_ENCODING_ALGO = 'HS256'
JWT_ENCODING_SECRET_KEY = 'Cyber@123'
JWT_TOKEN_EXPIRY_DELTA = 300000
AUTH_USER_MODEL = 'user_auth.User'

AUTHENTICATION_BACKENDS = ["utils.base_authentication.AuthenticationBackend"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xy!2(yr6ogb&aato)i)8v*!gkm#&ik)*ft-(fnvthb8*u#$)s)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_auth',
    'permissions',
    'hrm_app'
    # 'sessions',
    # 'myapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# # Function to wait for the database to be ready
# def wait_for_db():
#     db_up = False
#     while not db_up:
#         try:
#             conn = psycopg2.connect(
#                 dbname=os.getenv('DB_NAME', 'mydb'),
#                 user=os.getenv('DB_USER', 'mydb'),
#                 password=os.getenv('DB_PASSWORD', 'admin'),
#                 host=os.getenv('DB_HOST', 'db'),
#                 port=os.getenv('DB_PORT', '5432')
#             )
#             db_up = True
#         except psycopg2.OperationalError as e:
#             if "does not exist" in str(e):
#                 print('Database does not exist yet, waiting for 5 seconds...')
#             else:
#                 print('Database unavailable, waiting for 5 seconds...')
#             time.sleep(10)
#     conn.close()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME', 'mydb'),
#         'USER': os.getenv('DB_USER', 'mydb'),
#         'PASSWORD': os.getenv('DB_PASSWORD', 'admin'),
#         'HOST': os.getenv('DB_HOST', 'db'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }

# # Wait for the database to be ready
# wait_for_db()

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # Redis settings for Celery
# CELERY_BROKER_URL = 'redis://redis:6379/0'  # Ensure this matches the Redis service in docker-compose
# CELERY_RESULT_BACKEND = 'redis://redis:6379/0'  # Optional, but useful if you want to store results in Redis

# # Optional Celery settings:
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'  # Adjust if you have a different timezone


# Celery settings
# CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as broker
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Store results in Redis

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
# Email backend settings (for sending emails)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Use your email provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'syedjawadali92@gmail.com'  # Your email
EMAIL_HOST_PASSWORD = 'ctpgxfclwyucweni'  # Your email password
DEFAULT_FROM_EMAIL = 'your_email@example.com' 