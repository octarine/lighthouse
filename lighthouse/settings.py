# (c) Crown Owned Copyright, 2016. Dstl.
"""
Django settings for lighthouse project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# Default to showing debug pages on error. Set the environment variable to any
# other value to turn it off (which we want in production).
DEBUG = os.getenv('LIGHTHOUSE_DEBUG', 'True') == 'True'
# Default to an empty array (for development and test), but otherwise read from
# an environment variable.
ALLOWED_HOSTS = os.getenv('LIGHTHOUSE_ALLOWED_HOSTS', '').split(',')


# default for use in development, separate from actual production key
if DEBUG:
    SECRET_KEY = 'h)9lw!5*s@zz3rfz*za(b%eda_$k%9tm1tguhd2gre4l0ykoke'
else:
    SECRET_KEY = os.getenv('LIGHTHOUSE_SECRET_KEY')


# Application definition
INSTALLED_APPS = [
    # django provided
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'compressor',
    'haystack',
    'taggit',

    # this project
    'acceptancetests',
    'apps.accounts',
    'apps.access',
    'apps.govuk_template',
    'apps.home',
    'apps.links',
    'apps.organisations',
    'apps.search',
    'apps.teams',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lighthouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.govuk_template.variables.globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'lighthouse.wsgi.application'

# WARNING: This is probably too much for production
COMPRESS_REBUILD_TIMEOUT = 2


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('LIGHTHOUSE_DB', 'lighthouse'),
        'USER': os.getenv('LIGHTHOUSE_DB_USER', 'lighthouse'),
        'PASSWORD': os.getenv('LIGHTHOUSE_DB_PASSWORD', ''),
        'HOST': os.getenv('LIGHTHOUSE_DB_HOST', ''),
        'PORT': os.getenv('LIGHTHOUSE_DB_PORT', ''),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'accounts.User'

domain = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': '{}.UserAttributeSimilarityValidator'.format(domain)},
    {'NAME': '{}.MinimumLengthValidator'.format(domain)},
    {'NAME': '{}.CommonPasswordValidator'.format(domain)},
    {'NAME': '{}.NumericPasswordValidator'.format(domain)},
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.getenv('LIGHTHOUSE_STATIC_ROOT', None)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "apps/govuk_frontend_toolkit/stylesheets"),
    os.path.join(BASE_DIR, "apps/govuk_frontend_toolkit/images"),
    os.path.join(BASE_DIR, "apps/govuk_frontend_toolkit/javascripts"),
    os.path.join(BASE_DIR, "apps/govuk_elements/public/sass"),
    os.path.join(BASE_DIR, "sass"),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

COMPRESS_ROOT = os.path.join(BASE_DIR, "sass")

COMPRESS_ENABLED = True

# SASS
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Enable pretty and useful colourful tests

TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

LOGIN_URL = '/login'

# Search
WHOOSH_INDEX = os.path.join(os.path.dirname(__file__), 'whoosh_index')
if 'test' in sys.argv:
    WHOOSH_INDEX = os.path.join(os.path.dirname(__file__), 'whoosh_test_index')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
