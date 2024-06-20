import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Replace with your secret key
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/smart'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
