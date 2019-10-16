from logging import getLogger
from pathlib import Path
import os
import json

import appdirs

import something

logger = getLogger(__name__)


class FlaskConfig:
    """
    Flask base config settings
    """

    HOST = "0.0.0.0"
    DATA_DIR = appdirs.site_data_dir(something.__name__, something.__author__)


class DevConfig(FlaskConfig):
    """
    Default dev config
    """

    ENV = "development"
    DEBUG = True


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
    # Try to load in user config file; otherwise, use production config
    try:
        config_dir = Path(
            appdirs.site_config_dir(something.__name__, something.__author__)
        )
        config_path_py = config_dir.joinpath("config.py")
        config_path_json = config_dir.joinpath("config.json")

        if config_path_py.exists():
            app.config.from_pyfile(config_path_py, silent=True)
            logger.info(f"Using system config found at ${config_path_py}")
        elif config_path_json.exists():
            app.config.from_json(config_path_json)
            logger.info(f"Using system config found at ${config_path_json}")
        else:
            raise FileNotFoundError("No system config found")  # caught in IOError
    except (IOError, json.decoder.JSONDecodeError):
        # Load in an instance of a default config
        config = {
            "production": ProdConfig,
            "development": DevConfig,
            "testing": TestConfig,
        }[os.environ.get("SOMETHING_ENV", "production")]()
        app.config.from_object(config)
        logger.warning("Failed to load config, using defaults")
