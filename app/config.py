import os

class Config(object):
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')
    DB_PATH = '/home/bolha-dev/app/data/bolha_dev.db'

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
