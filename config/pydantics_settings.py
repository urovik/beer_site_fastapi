
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):


    model_config = SettingsConfigDict(env_file='fastapi_app/.env', env_file_encoding='utf-8')

class DbConfig(Settings):
    host: str
    db_name: str
    user_db: str
    password_db: str


class JWTConfig(Settings):  
    secret_key: str
    secret_public_key: str 
    algorithm: str = "RS256"
    expire_minutes: int = 20

jwt_config = JWTConfig()
db_config = DbConfig()
