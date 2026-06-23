from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lkad=lg^y96_nwk^3nef(po%%^7du*ar6b1b-*g84&i01e)+xw"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
SITE_ID = 2


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",  # ✅ REQUIRED
    "django.contrib.messages",  # ✅ REQUIRED
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_extensions",
    "debug_toolbar",
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',
    # MY APPS
    "shop",
    "acounts",
    "dashboard",
]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_SQL': True,
    'SHOW_STATICIP': True,
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # ✅ REQUIRED
    "django.middleware.common.CommonMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # ✅ REQUIRED
    "django.contrib.messages.middleware.MessageMiddleware",  # ✅ REQUIRED
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware"

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = "my_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "shop/templates",
            BASE_DIR / "acounts/templates",
            BASE_DIR / "dashboard/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",  # ✅ REQUIRED
                "django.contrib.messages.context_processors.messages",  # ✅ REQUIRED
            ],
        },
    },
]

WSGI_APPLICATION = "my_shop.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "shop/static",
    BASE_DIR / "acounts/static",
]
INTERNAL_IPS = ["127.0.0.1",]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
JAZZMIN_SETTINGS = {
    "site_title": "Panj Shanbe Bazar",
    "site_header": "Panj Shanbe Bazar",
    "site_brand": "Panj Shanbe Bazar",
    "welcome_sign": "Welcome to Admin panel",
    "site_logo": "icons/android-chrome-192x192.png",
    "show_ui_builder": True,
    "order_with_respect_to": [
        "shop",
        "acounts",
        "dashboard",
    ],
}
AUTH_USER_MODEL="acounts.user"
#allauth settings

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False