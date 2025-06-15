
from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# List of hosts/domain names that this Django site can serve.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.153.6','192.168.43.6']


# Application definition
INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'main',
    'users',
    'events',
    'chatapp',
    'Travels',

    # Third-party apps
    'tinymce',
    'fontawesomefree',
    'crispy_forms',
    'captcha',
    'crispy_bootstrap4',
    
    

    # Django Allauth apps
    'django.contrib.sites',  # Ensure 'sites' app is included
    'allauth',
    'allauth.account',
    'channels',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

ASGI_APPLICATION = 'djang_website.asgi.application'

WSGI_APPLICATION = 'djang_website.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Enable social login on GET request (not recommended for production)
SOCIALACCOUNT_LOGIN_ON_GET = True

# Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Django Allauth middleware
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'djang_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add your custom template directories if any
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




# Database configuration (SQLite as default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Crispy Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default redirect URL after login
LOGIN_REDIRECT_URL = '/'

# URL for login page
LOGIN_URL = 'login'

# Set a valid site ID for Django Allauth
SITE_ID = 3

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Django Allauth authentication backend
)

# Configure Google provider for Django Allauth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Recaptcha keys
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')

# Silence captcha test key error
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Media files settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Use config to maintain consistency
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Use the same email as the default sender



# Password reset timeout (in seconds)
PASSWORD_RESET_TIMEOUT = 864000  # 10 days


# TinyMCE settings (example configuration)
TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    'menubar': 'file edit view insert format tools table help',
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
                '| bullist numlist | outdent indent | table | link image | codesample | preview code | tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': '8pt 10pt 12pt 14pt 16pt 18pt',
    'content_style': 'body { font-family: Arial; background: white; color: black; font-size: 12pt}',
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'},
        {'text': 'HTML/XML', 'value': 'markup'},
    ],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {}}],
    'width': 'auto',
    'height': '600px',
    'image_caption': True,
    'images_upload_url': 'upload_image',
}

# Twilio settings
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER')


# >>> Site.objects.all()
# <QuerySet [<Site: 127.0.0.1:8000>]>
# >>> from django.contrib.sites.models import Site
# >>> site = Site.objects.all()[0]
# >>> print(site.id)
# 3
# >>>
