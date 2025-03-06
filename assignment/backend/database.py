# import os
# import psycopg2
# from psycopg2 import sql

# DATABASE_URL = os.getenv('postgresql://postgres:postgres@postgres:5432/app_db')

# def get_db_connection():
#     return psycopg2.connect(DATABASE_URL)

import os
import psycopg2

def get_db_connection():
    # Try to get the DATABASE_URL from environment variables
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        # Connect using the DATABASE_URL if available
        conn = psycopg2.connect(database_url)
    else:
        # Fallback to individual connection parameters
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "postgres"),
            database=os.getenv("POSTGRES_DB", "app_db"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
    
    return conn