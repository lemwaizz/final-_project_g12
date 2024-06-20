import os
from dotenv import load_dotenv


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bd86fcda4e34376994502b606e987c55')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://uerc0sc865i3pi:p56c4181667363c1e9b7d1505af1386e8819073cb3f8771419d172f6a8a9bf913@c97r84s7psuajm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dfhg82te2eb5m3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'b1e5b8f403fae1d779df7607be9b0f08')
