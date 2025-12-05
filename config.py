import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET _KEY') or 'dev-secret-change-in-production'

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///records.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False