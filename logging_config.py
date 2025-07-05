"""ロギング設定を管理するモジュール。"""

import logging
import logging.config
import sys

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simpleFormatter": {
            "format": (
                "%(levelname)-8s %(asctime)s %(module)s "
                "%(process)s %(pathname)s:%(lineno)d %(message)s"
            )
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simpleFormatter",
            "stream": sys.stdout,
        },
        "fileHandler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simpleFormatter",
            "filename": "logs/python.log",
            "when": "MIDNIGHT",
            "interval": 1,
        },
    },
    "loggers": {
        "": {  # root logger
            "level": "DEBUG",
            "handlers": ["consoleHandler", "fileHandler"],
            "propagate": True,
        },
        "hoge": {
            "level": "DEBUG",
            "handlers": ["consoleHandler", "fileHandler"],
            "propagate": False,
        },
    },
}


def setup_logging():
    """ロギング設定を初期化する。"""
    logging.config.dictConfig(LOGGING_CONFIG)
