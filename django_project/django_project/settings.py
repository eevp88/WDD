"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

def look_folder_tree(root):
    result = ()
    for dir_name, sub_dirs, file_names in os.walk(root):
        for sub_dir_name in sub_dirs:
            result += (os.path.join(dir_name, sub_dir_name),)
    return result

# Django settings for project.

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zAglvl5YntDbLA2FAud91VviB12qcEd7OFCxolKPxO0KTMqS6b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['104.236.82.89']
#Email config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.office365.com'

EMAIL_HOST_USER= 'infoder@uach.cl'

EMAIL_HOST_PASSWORD = 'p4r4l3l0'

EMAIL_PORT = 587

EMAIL_USE_TLS= True

# Application definition

GRAPPELLI_ADMIN_TITLE='Doctorado en Derecho'

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'userprofile',
    'documentos',
)

MIDDLEWARE_CLASSES = (
     'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'ElMMNEMfdN',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


#STATICFILES_DIRS=(
#	os.path.join(BASE_DIR, 'static'),
#	STATIC_ROOT,
#)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

STATIC_URL = '/static/'


STATIC_ROOT =  os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static'])
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['media'])
MEDIA_URL = '/media/'
STATICFILES_DIRS= look_folder_tree(STATIC_ROOT)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
	'django.core.context_processors.request',
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

