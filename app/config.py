class Config:
    SECRET_KEY= '0725932962'

class ProdConfig(Config):
    """"""
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://password@hostname:port/databasename'
    DEBUG = True

config_options = {
    'prod':ProdConfig, 
    'dev':DevConfig
}    