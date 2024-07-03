"""
Django settings for djang_website project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(c@9=wl&3=c#nm@=5#hn$#dpw5zqm0vvmojfcr!d7%&7&ofz2n'

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
    # Add our new application
    'main',
    'users',
    'tinymce',
    'fontawesomefree',
    'crispy_forms',
    'captcha',
    'crispy_bootstrap4',
    'django.contrib.sites',  # Ensure 'sites' app is included
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_LOGIN_ON_GET=True
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'djang_website.urls'

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

WSGI_APPLICATION = 'djang_website.wsgi.application'

# settings.py

TWILIO_ACCOUNT_SID = '##############'
TWILIO_AUTH_TOKEN = '########'
TWILIO_PHONE_NUMBER = '+#########'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = 'login'

SITE_ID = 1  # Ensure a valid site ID is set

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'  # Example redirect URL after login

# Configure Google provider
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

RECAPTCHA_PUBLIC_KEY = '$$$$$$$$$$$$$$$$$$'
RECAPTCHA_PRIVATE_KEY = '##########-2-##########'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'smartsaran3031@gmail.com'
EMAIL_HOST_USER = 'smartsaran3031@gmail.com'
EMAIL_HOST_PASSWORD = '############'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 14400

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880 # 5MB

TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    "menubar": "file edit view insert format tools table help",
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt",
    'content_style': "body { font-family: Arial; background: white; color: black; font-size: 12pt}",
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'}, {'text': 'HTML/XML', 'value': 'markup'},],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {} }],
    'width': 'auto',
    "height": "600px",
    'image_caption': True,
    "images_upload_url": "upload_image",
}