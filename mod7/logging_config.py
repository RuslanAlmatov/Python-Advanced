import sys

from layered_handler import *

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "'%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'"
        }
    },
    "handlers": {
        "custom_handlers": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
        },
        "layred_handler": {
            "()": LayredHandler,
            "level": "DEBUG",
            "formatter": "base"
        }
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["custom_handlers", "layred_handler"]
        }
    },
}
