import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    # Heroku PostgreSQL database URL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    

