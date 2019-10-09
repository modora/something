from logging import getLogger
from pathlib import Path
import os
import json

import something
from something import app

logger = getLogger(__name__)

if __name__ == "__main__":
    # Try to load in user config file; otherwise, use production config
    try:
        # TODO: Load user config
        _is_default_config = False  # is default config
        config_dir = Path(something.app_dirs.site_config_dir)
        config_path_py = config_dir.joinpath('config.py')
        config_path_json = config_dir.joinpath('config.json')

        if config_path_py.exists():
            app.config.from_pyfile(config_path_py, silent=True)
            logger.info(f"Using system config found at ${config_path_py}")
        elif config_path_json.exists():
            app.config.from_json(config_path_json)
            logger.info(f"Using system config found at ${config_path_json}")
        else:
            raise FileNotFoundError("No system config found")
    except (IOError, json.decoder.JSONDecodeError) as e:
        # Load in an instance of a default config
        config = {
            'production': something.config.ProdConfig,
            'development': something.config.DevConfig,
            'testing': something.config.TestConfig
        }[os.environ.get('SOMETHING_ENV', 'production')]()
        app.config.from_object(config)
        logger.warning("Failed to load config, using defaults")
    
    app.run(host=app.config.get('HOST'))
