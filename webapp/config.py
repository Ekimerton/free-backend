import os

class Config:
    DEBUG = True
    # App
    try:
        SECRET_KEY = os.environ['SECRET_KEY']
    except:
        SECRET_KEY = "test"

    # Database
    # SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
