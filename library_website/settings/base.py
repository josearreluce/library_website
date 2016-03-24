"""
Django settings for library_website project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',

    'taggit',
    'compressor',
    'modelcluster',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsearch',
    'wagtail.wagtailimages',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailembeds',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.wagtailsearchpromotions',
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.wagtailstyleguide',
    'wagtail.contrib.wagtailapi',

    'rest_framework',
    'ask_a_librarian',
    'base',
    'conferences',
    'directory_unit',
    'group',
    'home',
    'icon_list_boxes',
    'intranetforms',
    'intranethome',
    'intranettocs',
    'intranetunits',
    'lib_collections',
    'library_website',
    'news',
    'public',
    'projects',
    'search',
    'shibboleth',
    'staff',
    'subjects',
    'units',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    # Required for shibboleth
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shibboleth.middleware.ShibbolethRemoteUserMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'library_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shibboleth.context_processors.login_link',
                'shibboleth.context_processors.logout_link',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Don't put database information here!!!


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Phone number format
PHONE_FORMAT = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
PHONE_ERROR_MSG = 'Please enter the phone number using the format 773-123-4567'

# Postal code format
POSTAL_CODE_FORMAT = '^[0-9]{5}$'
POSTAL_CODE_ERROR_MSG = 'Please enter the postal code as a five digit number, e.g. 60637'

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Wagtail settings
WAGTAIL_SITE_NAME = "library_website"

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
    	'URLS': ['http://localhost:9200'],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
    }
}

# Lock down specific nodes to wagtail groups. Sections are locked down
# by page ID. In order to see any page, a user must belong to all groups
# set in all page ancestors. This works as a blacklist. 
# PERMISSIONS_MAPPING = {6: ['Library'], 319: ['Foo', 'Bar']}
PERMISSIONS_MAPPING = {6: ['Library']}

# Where to send users that aren't members of the necessary groups to
# view a page.
NO_PERMISSIONS_REDIRECT_URL = 'https://motacilla.lib.uchicago.edu/no-permission/'

# Settings for RESTful API and frontend cache invalidation
WAGTAILAPI_SEARCH_ENABLED = True
WAGTAILAPI_MAX_RESULTS = 60

# Institutional ID for libcal
LIBCAL_IID = 482

# Fallback unit for pages that don't have one
DEFAULT_UNIT = 2235

# String template for hours display in header
HOURS_TEMPLATE = '%s: %s'
