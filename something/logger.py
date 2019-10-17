from pathlib import Path
from logging import getLogger
import logging.config

def _is_file_handler(settings):
    """
    Checks if the handler given is a python logging handler

    :settings:      handler settings
    """
    FILE_HANDLERS = [
                "logging.FileHandler",
                "logging.handlers.WatchedFileHanlder",
                "logging.handlers.BaseRotatingHandler",
                "logging.handlers.RotatingFileHandler",
                "logging.handlers.TimedRotatingFileHandler",
            ]
    
    if settings['class'] in FILE_HANDLERS:
        return True
    return False

def _resolve_file_handler_paths(app, config):
    # update file handlers such that all paths are absolute. Relative paths will
    # be resolved relative to the DATA_DIR config option
    # TODO: Security - Prevent relative paths as inputs
    for handler, settings in config["handlers"].items():
        if  _is_file_handler(settings) and not Path(settings["filename"]).is_absolute():
            # update config to replace filename as absolute path
            config["handlers"][handler]["filename"] = Path(
                app.config.get("DATA_DIR")
            ).joinpath(settings["filename"])

def _initialize_log_file(config):
    """
    Creates the log file if it doesn't already exist
    """
    for settings in config['handlers'].values():
        if _is_file_handler(settings):
            log_path = Path(settings['filename'])
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_path.touch(exist_ok=True)

def configure_logger(app, logger=None):
    config = app.config.get("LOG_CONFIG")
    _resolve_file_handler_paths(app, config)
    _initialize_log_file(config)

    logging.config.dictConfig(config)
    return getLogger(logger)
