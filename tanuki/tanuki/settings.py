"""
Django settings for tanuki project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/


For Addison: cloud_sql_proxy.exe -instances="tanuki-58:us-central1:tanuki"=tcp:3306

For Pablo: cloud_sql_proxy.exe -instances="tanuki-58:us-central1:tanuki"=tcp:3306

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--j8t+_%uuh9wq)g)03wktyf529a1doax+0gaea7xmv77&ok^3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tanuki-58.uc.r.appspot.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'login',
    'overview',
    'budget',
    'history',
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

ROOT_URLCONF = 'tanuki.urls'

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
            ],

        },
    },

    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'jinja2/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'tanuki.jinja2.environment'
        },
    },
]



WSGI_APPLICATION = 'tanuki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# cloud_sql_proxy.exe -instances="tanuki-58:us-central1:tanuki"=tcp:3306 to start cloud proxy

if os.getenv('GAE_APPLICATION', None):
    DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'tanuki',
    #     'USER': 'postgres',
    #     'PASSWORD': 'codersdontwearsafetyglasses',
    #     'HOST': 'localhost',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '/cloudsql/tanuki-58:us-central1:tanuki',
        'USER': 'postgres',
        'PASSWORD': 'codersdontwearsafetyglasses',
        'NAME': 'tanuki',
    }
}

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'tanuki',
            'USER': 'postgres',
            'PASSWORD': 'codersdontwearsafetyglasses',
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

#Authentication Backend

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'login.backends.EmailAuthentication',
]

AUTH_USER_MODEL = 'login.User'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = 'login:index'
