from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

class DatabaseConfig:
    user = os.getenv('DB_USER')
    password = quote_plus(os.getenv('DB_PASSWORD'))
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    DATABASE_URL = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'

class JWTConfig:
    jwt_secret = os.getenv('JWT_SECRET')
    jwt_algorithm = os.getenv('JWT_ALGORITHM')
    jwt_access_token_expiry = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRY'))
    jwt_refresh_token_expiry = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRY'))


