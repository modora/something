from pathlib import Path
import os
import json
import collections

import appdirs

import something

# a dict that automatically creates parent keys on assignment
# https://stackoverflow.com/a/16724937
nested_dict = lambda: collections.defaultdict(nested_dict)


class FlaskConfig:
    """
    Flask base config settings
    """

    HOST = "0.0.0.0"
    DATA_DIR = appdirs.site_data_dir(something.__name__, something.__author__)
    # Config modified from https://stackoverflow.com/a/7507842
    LOG_CONFIG = nested_dict()
    LOG_CONFIG.update(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "INFO",
                    "formatter": "standard",
                    "filename": "something.log",
                    "maxBytes": 1024,
                    "backupCount": 3,
                }
            },
            "loggers": {
                "": {  # root logger
                    "handlers": ["default"],
                    "level": "DEBUG",
                    "propagate": True,
                }
            },
        }
    )


class DevConfig(FlaskConfig):
    """
    Default dev config
    """

    ENV = "development"
    DEBUG = True
    # add debug messeges to stdout
    LOG_CONFIG = FlaskConfig.LOG_CONFIG.copy()
    LOG_CONFIG["handlers"]["debug_stream"] = {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "standard",
        "stream": "ext://sys.stderr",  # log to stdout
    }
    LOG_CONFIG["loggers"][""]["handlers"].append("debug_stream")


class ProdConfig(FlaskConfig):
    """
    Default production config
    """

    ENV = "production"
    HOST = "127.0.0.1"


class TestConfig(FlaskConfig):
    """
    Default test config
    """

    ENV = "testing"
    DEBUG = True
    TESTING = True


def loadConfig(app):
    # Load in an default config
    config = {
        "production": ProdConfig,
        "development": DevConfig,
        "testing": TestConfig,
    }[os.environ.get("SOMETHING_ENV", "production")]()
    app.config.from_object(config)
    app.config["config_file"] = None
    
    # Try to load in user config file to override defaults
    config_dir = Path(
        appdirs.site_config_dir(something.__name__, something.__author__)
    )
    config_path_py = config_dir.joinpath("config.py")
    config_path_json = config_dir.joinpath("config.json")

    if config_path_py.exists():
        app.config.from_pyfile(config_path_py, silent=True)
        app.config["config_file"] = config_path_py
    elif config_path_json.exists():
        app.config.from_json(config_path_json)
        app.config["config_file"] = config_path_json
