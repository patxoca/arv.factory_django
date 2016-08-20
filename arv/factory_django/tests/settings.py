# -*- coding: utf-8 -*-

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

SECRET_KEY = "Tests don't require a really s3cr3t k3y ;)"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "tests",
)

SITE_ID = 1
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = ""
