# -*- encoding: utf-8 -*-
import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    BASE_DIR = '/home/linkedin-python-scrapy-scraper'
    db_name = 'database.db'
    db_path = os.path.join(BASE_DIR, db_name)
    db_path = "/home/linkedin-python-scrapy-scraper/myjobs.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')

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
