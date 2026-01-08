import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kunci_rahasia_anda_yang_sangat_aman_dan_panjang'
    
    # Database Configuration (from environment variables)
    DB_USER = os.environ.get('DB_USER') or 'postgres'
    DB_PASS = os.environ.get('DB_PASSWORD') or ''
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or '5432'
    DB_NAME = os.environ.get('DB_NAME') or 'postgres'

    # URL encode password to handle special characters
    # Add sslmode=require for Supabase connections
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or (
        f"postgresql://{DB_USER}:{quote_plus(DB_PASS)}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # SSL engine options for PostgreSQL
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "sslmode": "require"
        }
    }

    # Supabase Configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
    SUPABASE_BUCKET = os.environ.get('SUPABASE_BUCKET') or 'images'

