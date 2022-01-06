"""
Django settings for eshop project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.template.context_processors import static

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vz-yu&6ksxh3bay)uz_)hhq*q7^5%px=66o@hn%rtdjhgih%m%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    # apps
    'store',
    'customer',
    'custom.apps.CustomConfig',
    'ckeditor_uploader',
    'ckeditor',
    'orders',
    'frontend',
    'social_django',
    



]


CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    
    
]

ROOT_URLCONF = 'eshop.urls'

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
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

WSGI_APPLICATION = 'eshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eshopper',
        'USER': 'postgres',
        'PASSWORD': 'Neosoft$22',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
MEDIA_URL='/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL='home'
# LOGOUT_REDIRECT_URL='loginpage'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    

    
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_TWITTER_KEY = 'MMYUz7Avt3XRoQwExEoZOeiOE'
SOCIAL_AUTH_TWITTER_SECRET='TVkCSGLDsWGKL6bIMvAm27xQd2ryAOMSaUPKIxIgdWrMzAltjj'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='1009203020192-f8oop3ito9f1tr7k6dfthni517ug5h88.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='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'

LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

#SMTP Config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'raulshivani06@gmail.com'
EMAIL_HOST_PASSWORD = '9821019851'


SITE_ID = 1


MAILCHIMP_API_KEY = '96d513438472b0fc929feaca91506392-us20'
MAILCHIMP_DATA_CENTER = 'us20'
MAILCHIMP_EMAIL_LIST_ID ='02294f12e1'