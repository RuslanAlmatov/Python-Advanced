import logging.handlers
import sys

from layered_handler import *
from ASCII_Filter import *

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
        },
        "utils_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "H",
            "interval": 10,
            "backupCount": 1,
            "formatter": "base",
            "level": "INFO",
            "filename": "utils.log"
        },
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["custom_handlers", "layred_handler"]
        },
        "utils": {
            "level": "INFO",
            "handlers": ["utils_handler"]
        }
    },
    "filters": {
        "ascii_filter": {
            "()": ASCIIFilter,
        }
    }
}
