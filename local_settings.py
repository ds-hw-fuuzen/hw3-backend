import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DEV_DB_NAME", ""),  # noqa
        "USER": os.getenv("DEV_DB_USER", ""),
        "PASSWORD": os.getenv("DEV_DB_PASSWORD", ""),
        "HOST": os.getenv("DEV_DB_HOST", ""),
        "PORT": os.getenv("DEV_DB_PORT", ""),
    },
}