import os
from dotenv import load_dotenv



load_dotenv()

class Settings():
    password_db = os.getenv('PASSWORD_DB')
    name_db = os.getenv('DB_NAME')
    host_db = os.getenv('HOST')
    user_db = os.getenv('USER_DB') 
    private_key = os.getenv('PRIVATE_KEY').strip()
    public_key = os.getenv('PUBLIC_KEY').strip()
    algorithm = os.getenv('ALGORITHM')
    expire_minutes = os.getenv('EXPIRE_MINUTES')

