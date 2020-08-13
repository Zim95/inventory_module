from dotenv import load_dotenv
import os


BASE_DIR = os.path.abspath('')
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=ENV_PATH)


class BaseConfig(object):
    APP_SETTINGS = os.environ.get("APP_SETTINGS", None)
    FLASK_APP = os.environ.get("FLASK_APP", None)
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.environ.get("SECRET", None)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", None)


class TestConfig(BaseConfig):
    DEBUG = True
    TEST = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL", None)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TEST = False


class StagingConfig(BaseConfig):
    DEBUG = True
    TEST = False


class ProductionConfig(BaseConfig):
    TEST = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
