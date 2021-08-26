import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True     #DEBUG: setting this to True activates the debug mode on the app. This allows us to use the Flask debugger in case of an unhandled exception.
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'signup'
    DATABASE_PASSWORD = '1234'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"


class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'cr'
    DATABASE_PASSWORD = 'devadmin@098'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "app.log"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_USER    : export user name              :       "root"
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export databse URI            :       IP Address
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_URI = os.environ.get("DATABASE_URI")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    LOG_FILE = "app.log"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
