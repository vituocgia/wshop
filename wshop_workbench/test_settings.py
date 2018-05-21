# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import os

BASE_DIR = os.getenv("WSHOP_WORKBENCH_BASE_DIR") or (
    os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = "Shhhhh"
DEBUG = True
ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(BASE_DIR, "var", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "var", "static")
MEDIA_URL = "/media/"

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # external apps that needs to be loaded before Wshop
    'easy_thumbnails',
    # wshop themes
    'wshop.themes.classic_gray',
    # wshop
    'wshop.core',
    'wshop.admin',
    'wshop.api',
    'wshop.addons',
    'wshop.default_tax',
    'wshop.front',
    'wshop.front.apps.auth',
    'wshop.front.apps.carousel',
    'wshop.front.apps.customer_information',
    'wshop.front.apps.personal_order_history',
    'wshop.front.apps.saved_carts',
    'wshop.front.apps.registration',
    'wshop.front.apps.simple_order_notification',
    'wshop.front.apps.simple_search',
    'wshop.front.apps.recently_viewed_products',
    'wshop.notify',
    'wshop.simple_cms',
    'wshop.customer_group_pricing',
    'wshop.campaigns',
    'wshop.simple_supplier',
    'wshop.order_printouts',
    'wshop.testing',
    'wshop.utils',
    'wshop.xtheme',
    'wshop.reports',
    'wshop.default_reports',
    'wshop.regions',
    'wshop.importer',
    'wshop.default_importer',
    # external apps
    'bootstrap3',
    'django_countries',
    'django_jinja',
    'filer',
    'registration',
    'rest_framework',
    'rest_framework_swagger'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wshop.front.middleware.ProblemMiddleware',
    'wshop.core.middleware.WshopMiddleware',
    'wshop.front.middleware.WshopFrontMiddleware',
    'wshop.xtheme.middleware.XthemeMiddleware',
    'wshop.admin.middleware.WshopAdminMiddleware'
]

ROOT_URLCONF = 'wshop_workbench.test_urls'
WSGI_APPLICATION = 'wshop_workbench.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
SOUTH_TESTS_MIGRATE = False  # Makes tests that much faster.
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {'format': '[%(asctime)s] (%(name)s:%(levelname)s): %(message)s'},
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'wshop': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True},
    }
}

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('ja', 'Japanese'),
    ('zh-hans', 'Simplified Chinese'),
    ('pt-br', 'Portuguese (Brazil)'),
    ('it', 'Italian'),
]

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "wshop.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "debug": DEBUG
        }
    },
]

# set login url here because of `login_required` decorators
LOGIN_URL = "/login/"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

WSHOP_PRICING_MODULE = "customer_group_pricing"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'wshop.api.permissions.WshopAPIPermission',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [
        "get"
    ]
}

# extend the submit methods only if DEBUG is True
if DEBUG:
    SWAGGER_SETTINGS["SUPPORTED_SUBMIT_METHODS"].extend(["post", "patch", "delete", "put"])

WSHOP_SETUP_WIZARD_PANE_SPEC = [
    "wshop.admin.modules.shops.views:ShopWizardPane",
    "wshop.admin.modules.service_providers.views.PaymentWizardPane",
    "wshop.admin.modules.service_providers.views.CarrierWizardPane",
    "wshop.xtheme.admin_module.views.ThemeWizardPane",
    "wshop.admin.modules.content.views.ContentWizardPane",
    "wshop.admin.modules.sample_data.views.SampleObjectsWizardPane"
]


WSHOP_ERROR_PAGE_HANDLERS_SPEC = [
    "wshop.admin.error_handlers:AdminPageErrorHandler",
    "wshop.front.error_handlers:FrontPageErrorHandler"
]

WSHOP_SIMPLE_SEARCH_LIMIT = 150


if os.environ.get("WSHOP_WORKBENCH_DISABLE_MIGRATIONS") == "1":
    from wshop_workbench.settings.utils import DisableMigrations
    MIGRATION_MODULES = DisableMigrations()


def configure(setup):
    setup.commit(globals())
