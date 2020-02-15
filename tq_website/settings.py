"""
Django settings for tq project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import raven

ugettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("TQ_DEBUG", 'False') == 'True')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


ALLOWED_HOSTS = [
    # with . at beginning allows domain and subdomains
    # with . at end allows FQDN
    '.tq.ethz.ch.',
    '.tq.vseth.ch.',
    '.tq.vseth.ethz.ch.',
    '.tanzquotient.vseth.ethz.ch.',
    '.tanzquotient.org',
    '46.231.204.51',
    '192.168.99.100',
    '127.0.0.1', 'localhost',
]
# This should be set to true since we use NGINX as a proxy
USE_X_FORWARDED_HOST = True

# Application definition
INSTALLED_APPS = []

if not DEBUG:
    INSTALLED_APPS += [
        'raven.contrib.django.raven_compat',
    ]

INSTALLED_APPS += [
    'treebeard',
    'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry
    'filer',
    'easy_thumbnails',
    'djangocms_googlemap',
    'djangocms_link',
    'cms',  # django CMS itself
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',
    'bootstrap3',
    # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'reversion',
    'django_celery_beat',
    'django_celery_results',
    'djcelery_email',
    'post_office',
    'daterange_filter',
    'guardian',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_countries',
    'tq_website',
    'courses',
    'faq',
    'organisation',
    'events',
    'payment',
    'cms_plugins',
    'analytical',
    'rest_framework',
    'parler',
    'survey',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = int(os.environ.get("TQ_SITE_ID", 100))

ROOT_URLCONF = 'tq_website.urls'

WSGI_APPLICATION = 'tq_website.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FORMAT_MODULE_PATH = [
    'tq_website.formats',
]

# loopback and docker gateway
INTERNAL_IPS = ['127.0.0.1', '::1', '172.18.0.1']

###############################################
# Configuration of allauth account management #
###############################################
ANONYMOUS_USER_ID = -1

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
# default redirect URL after login (if no GET parameter next is given)
LOGIN_REDIRECT_URL = "/profile/dashboard"

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'TQ '
# ACCOUNT_LOGIN_ON_PASSWORD_RESET=True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_USER_DISPLAY = lambda user: user.first_name if user.first_name else user.email
ACCOUNT_SIGNUP_FORM_CLASS = 'courses.forms.CustomSignupForm'
ACCOUNT_LOGOUT_ON_GET = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# general cross-used static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':
                [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                    'sekizai.context_processors.sekizai',
                    'cms.context_processors.cms_settings',
                    'absolute.context_processors.absolute',
                ]
        }
    },
]

############################################
# Configuration of djangocms-text-ckeditor #
############################################
CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' ## DO NOT LOAD twice since already loaded in template!
CKEDITOR_IMAGE_BACKEND = 'pillow'

toolbar = [
    ['Undo', 'Redo'],
    ['cmsplugins', '-', 'ShowBlocks'],
    ['Format', 'Styles'],
    ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
    ['Maximize'],
    '/',
    ['Source'],
    '/',
    ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
    ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
    ['HorizontalRule'],
    ['NumberedList', 'BulletedList', 'Blockquote', '-', 'Outdent', 'Indent', '-', 'Table', 'Link', 'Unlink'],
]

# useful documentation about CKEditor:
# https://docs.ckeditor.com/#!/guide/dev_toolbarconcepts
# complete list of all available toolbar elements:
# https://ckeditor.com/forums/CKEditor/Complete-list-of-toolbar-items
# documentation for Django CMS plugin:
# https://pypi.python.org/pypi/djangocms-text-ckeditor/
CKEDITOR_SETTINGS = {
    'disableNativeSpellChecker': False,
    'language': 'en',
    'toolbar_CMS': toolbar,
    'toolbar_HTMLField': toolbar,
    'skin': 'moono-lisa'
}

###############################
# Configuration of django-cms #
###############################
CMS_TEMPLATES = (
    ('template_basic.html', 'Basic Template'),
    ('template_sidebar.html', 'Sidebar Template'),
)

LANGUAGES = [
    ('de', ugettext('Deutsch')),
    ('en', ugettext('English')),
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'de', },
        {'code': 'en', },
    ),
}

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': ugettext('Deutsch'),
            'fallbacks': ['en', ],
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': False,
        },
        {
            'code': 'en',
            'name': ugettext('English'),
            'fallbacks': ['de', ],
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': False,
        },
    ],
    'default': {
        'fallbacks': ['en', 'de', ],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    }
}

CMS_PLACEHOLDER_CONF = {
    'cms_content': {
        'name': ugettext('Main content'),
        'language_fallback': True,
    },
    'side_content': {
        'name': ugettext('Side content'),
        'language_fallback': True,
    },
    'title': {
        'name': ugettext('Title'),
        'language_fallback': True,
        'plugins': ['PageTitlePlugin'],
        'limits': {
            'PageTitlePlugin': 1,
        },
        'default_plugins': [
            {
                'plugin_type': 'PageTitlePlugin',
                'values': {},
            },
        ],
        'child_classes': {
            'PageTitlePlugin': ['ButtonPlugin', ],
        },
        'parent_classes': {
            'ButtonPlugin': ['PageTitlePlugin'],
        },
    },
}

##########################
# Configuration of filer #
##########################
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

##################################################
# Configuration of post_office plugin und celery #
##################################################

# Celery
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_RESULT_BACKEND = 'django-db'
BROKER_URL = "redis://redis/"
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# using post office as the default email backend 
EMAIL_BACKEND = 'post_office.EmailBackend'

POST_OFFICE = {
    'BACKENDS': {
        # using djcelery's email backend as a backend for post office
        'default': 'djcelery_email.backends.CeleryEmailBackend',
    },
    'DEFAULT_PRIORITY': 'now'
}

###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'file_django': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'file_tq': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'tq.log'),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'file_payment': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'payment.log'),
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'errors.log'),
            'maxBytes': 50000000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        # this top level logger logs ALL messages
        '': {
            'handlers': ['mail_admins', 'file_errors'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'tq': {
            'handlers': ['file_tq', 'console'],
            'level': 'DEBUG',
        },
        'payment': {
            'level': 'DEBUG',
            'handlers': ['console', 'file_payment', ],
        },
        'django': {
            'handlers': ['file_django', 'console'],
            'level': 'INFO',
        },
    }
}

##################
# REST FRAMEWORK #
##################
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

##########
# PARLER #
##########
PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'en', },
        {'code': 'de', },
    ),
    'default': {
        'fallbacks': ['de', 'en'],  # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,  # the default; let .active_translations() return fallbacks too.
    }
}

# Path for translation files
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

#################
# Debug Toolbar #
#################

DEBUG_TOOLBAR_PATCH_SETTINGS = False  # configure manually and do not let debug-toolbar autopatch my settings!
# Show toolbar whenever DEBUG is True. Workaround for dynamic IPs in a Docker environment (which would not be in INTERNAL_IPS)
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("TQ_SECRET_KEY", '')

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'tq_website',
    } if DEBUG else {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
    'db': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'tq_cache_table',
    }
}

# Configure the email host to send mails from
EMAIL_HOST = os.environ.get("TQ_EMAIL_HOST", '')
EMAIL_HOST_USER = os.environ.get("TQ_EMAIL_HOST_USER", '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ.get("TQ_EMAIL_HOST_PASSWORD", '')
DEFAULT_FROM_EMAIL = os.environ.get("TQ_DEFAULT_FROM_EMAIL", '')

ADMINS = [(email, email) for email in os.environ.get("TQ_ADMINS", "").split(',')]
SERVER_EMAIL = os.environ.get("TQ_SERVER_EMAIL", 'test@example.com'),

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get("TQ_DB_HOST", 'tq-mysql'),
        'PORT': os.environ.get("TQ_DB_PORT", '3306'),
        'NAME': 'tq_website',
        'USER': os.environ.get("TQ_DB_USER", ''),
        'PASSWORD': os.environ.get("TQ_DB_PASSWORD", ''),
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get("TQ_DB_HOST_POSTGRES", 'tq-postgres'),
        'PORT': os.environ.get("TQ_DB_PORT_POSTGRES", '5432'),
        'NAME': 'tq_website',
        'USER': os.environ.get("TQ_DB_USER_POSTGRES", ''),
        'PASSWORD': os.environ.get("TQ_DB_PASSWORD_POSTGRES", ''),
    }
}

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get("TQ_GOOGLE_ANALYTICS_PROPERTY_ID", '')

# Postfinance Backend
FDS_HOST = 'fdsbc.post.ch'
FDS_USER = os.environ.get("TQ_FDS_USER", '')
FDS_PRIVATE_KEY = os.path.join(BASE_DIR, 'credentials', 'tq')
FDS_HOST_KEY = os.path.join(BASE_DIR, u'credentials', u'host_key')
FDS_DATA_PATH = 'fds_data'
FDS_PORT = 22

# Postfinance Account
PAYMENT_ACCOUNT = {
    'default': {
        'IBAN': os.environ.get("TQ_PAYMENT_ACCOUNT_IBAN", ''),
        'SWIFT': os.environ.get("TQ_PAYMENT_ACCOUNT_SWIFT", ''),
        'post_number': os.environ.get("TQ_PAYMENT_ACCOUNT_POST_NUMBER", ''),
        'recipient': ', '.join([os.environ.get("TQ_PAYMENT_ACCOUNT_RECIPIENT", ''),
                                os.environ.get("TQ_PAYMENT_ACCOUNT_RECIPIENT_ZIPCODE_CITY", '')])
    }
}

RAVEN_ENVIRONMENT = 'development' if DEBUG else 'production'

RAVEN_CONFIG = {
    'dsn': 'https://883ad6a3790e48aea0291f4a0d1d89c4:339fab1993244b4e9d414ebcef70cee0@sentry.io/124755',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.join(os.path.dirname(__file__), '..')),
    'environment': RAVEN_ENVIRONMENT
}
