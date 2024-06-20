import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'bd86fcda4e34376994502b606e987c55')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Heroku PostgreSQL database URL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'b1e5b8f403fae1d779df7607be9b0f08')

