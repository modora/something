from logging import getLogger
import os

import something
from something import app

logger = getLogger(__name__)

if __name__ == "__main__":
    # Try to load in user config file; otherwise, use production config
    try:
        # TODO: Load user config
        _is_default = False  # is default config
        raise FileNotFoundError("Not yet implemented")
    except FileNotFoundError:
        logger.info("User config not found, using defaults")
        _is_default = True
    except IOError:
        _is_default = True
        logger.warning("Failed to load config, using defaults")

    if _is_default:
        config = {
            'production': something.config.ProdConfig,
            'development': something.config.DevConfig,
            'testing': something.config.TestConfig
        }[os.environ.get('SOMETHING_ENV', 'production')]()
        app.config.from_object(config)
    
    app.run(host=app.config.get('HOST'))
