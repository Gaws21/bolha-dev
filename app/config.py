import os

class Config(object):
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')
    ROOT_DIR = os.getcwd()

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

user_agent_configs = {
    "mobile":{
        "home_page":"home_mobile.html",
        "first_result_page":"first_results_mobile.html",
        "search_result_page":"search_results_mobile.html",
        "pagination_size":37
    },
    "desktop":{
        "home_page":"home.html",
        "first_result_page":"first_results.html",
        "search_result_page":"search_results.html",
        "pagination_size":16
    },
}