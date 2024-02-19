import os

class Config(object):
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_PATH = 'data/bolha_dev.db'
    SQLALCHEMY_DATABASE_URI = f"{BASE_DIR}/{DB_PATH}"

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
