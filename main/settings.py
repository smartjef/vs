from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '102.37.21.185',
    'www.vstech.co.ke',
    'vstech.co.ke',
]

ADMINS = [
    ('Admin', 'o.jeff3.a@gmail.com'),
    ('Laurent', 'lawiomosh3@gmail.com'),
    ('Jeff', 'info@vstech.co.ke'),
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    'crispy_forms',
    'crispy_bootstrap5',
    'rest_framework',

    # Local apps
    'core.apps.CoreConfig',
    'project.apps.ProjectConfig',
    'users.apps.UsersConfig',
    'service.apps.ServiceConfig',
    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',
]

SITE_ID = 1

CART_SESSION_ID = 'cart'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processor.all',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': 5432,
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }


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


LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'sw'

THEME_CHOICES = [
    ('light', 'light'),
    ('dark', 'dark'),
]

LANGUAGES = [
    ('en', 'English'),
    ('sw', 'Swahili'),
]

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static/')
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_MAX_LENGTH = 200
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_MAX_EMAIL_ADDRESSES = 3
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1200
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_USERNAME_REQUIRED = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'VSTech Limited - '

CSRF_TRUSTED_ORIGINS = [
    'https://vstech.co.ke/',
    'https://www.vstech.co.ke/',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
