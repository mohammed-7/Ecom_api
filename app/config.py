import os 

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = "My_secret_key"
    JWT_SECRET_KEY = "JWT_secret_key" 
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False