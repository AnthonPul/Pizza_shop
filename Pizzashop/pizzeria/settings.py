"""
Django settings for pizzeria project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j@2bu)d(g+g%d&a($m803_351oc7ljng*r5y4^hmmxpa#b=351'

SOCIAL_AUTH_FACEBOOK_KEY = "519207226872671"
SOCIAL_AUTH_FACEBOOK_SECRET = "fab82ad1fdc422db938bb1223477b21c"
SOCIAL_AUTH_GOOGLE_KEY = '869017557035-tvl6pl70auslucjsdh7maam8i5mtt5av.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_SECRET = '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'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'acounts.User'

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'accounts',
    'address',
    'menu',
    'orders',
    'pages',
    'api',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'allauth.socialaccount.providers.facebook',
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

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'METHOD': 'oauth2',
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate',
            'access_type': 'online'
        },
        'FIELDS': [
            'email',
            'first_name',
            'last_name'
        ],
        'VERIFIED_EMAIL': False,
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': [
            'public_profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate',
            'access_type': 'online'
        },
        'FIELDS': [
            'email',
            'first_name',
            'last_name'
        ],
        'VERIFIED_EMAIL': False,
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'DjangoGoogleLogin.urls'

ROOT_URLCONF = 'pizzeria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
    
}

WSGI_APPLICATION = 'pizzeria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da0ph6rcefp02v',
        'USER': 'adfirdvohmhbzx',
        'PASSWORD': '734462e4e62c323fb6017aff3ae81c48fdeb23d688a1927cb8da3d09d33f874b',
        'HOST': 'ec2-3-223-242-224.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [
   # os.path.join(BASE_DIR, 'static'),
 #]
#=======

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
AUTH_USER_MODEL = 'accounts.User'


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'