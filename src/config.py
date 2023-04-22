import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Environment variables not loaded because .env file is missing')
else:
    load_dotenv()

MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD')
