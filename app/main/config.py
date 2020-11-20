import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class PostgresConfig(Config):
    DEBUG = True
    ENV = 'postgres-dev'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/Bookstore'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test-db.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/Bookstore'


config_by_name = dict(
    dev=DevelopmentConfig,
    postgres=PostgresConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
