"""
Default flask config settings
"""


class FlaskConfig:
    """
    Flask base config settings
    """
    HOST = "0.0.0.0"


class DevConfig(FlaskConfig):
    """
    Default dev config
    """
    ENV = 'development'
    DEBUG = True


class ProdConfig(FlaskConfig):
    """
    Default production config
    """
    ENV = 'production'
    HOST = "127.0.0.1"


class TestConfig(FlaskConfig):
    """
    Default test config
    """
    ENV = 'testing'
    DEBUG = True
    TESTING = True
