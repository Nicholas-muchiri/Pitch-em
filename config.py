import os

class Config:
    '''
    general configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nicholas:golfgti10@localhost/pitchem'
    
class DevConfig(Config):
    '''
    development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nicholas:golfgti10@localhost/pitchem'
    

config_options = {
'development':DevConfig,
'production':ProdConfig
}