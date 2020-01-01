"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

if os.path.exists('env.py'):
    import env
    
import dj_database_url    

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['pranita-tshirt-shop.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'ckeditor',
    'django.contrib.humanize',
    'storages',  
    
    # My own custom apps
    'home',
    'accounts',
    'feedback',
    'products',
    'contact',
    'cart',
    'checkout',
  
     
 
    
]

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default' : dj_database_url.parse(os.environ.get('DATABASE_URL'))
    } 
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}       


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=9460800',
}

AWS_STORAGE_BUCKET_NAME ="milestone-5-tshirt"

AWS_S3_REGION_NAME = 'eu-west-1'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_DEFAULT_ACL = None

STATICFILES_LOCATION = 'static'

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'shop/static')
]

#  Media Folder Settings

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

#  Testing - whether real email is sent

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587


# CKEDITOR CONFIGS

CKEDITOR_BASEPATH = "/'static'/ckeditor/ckeditor/"

CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_UPLOAD_PATH = "image_upload/"

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'height': 300,
        'width': 750,
        'toolbar':'Custom',
        'height': 'auto',
        'width': 'auto',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
        ]
    },
} 

# STRIPE KEYS

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')


