from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

class DatabaseConfig:
    load_dotenv()

    user = os.getenv("DB_USER")
    # password = os.getenv("DB_PASSWORD")
    password = quote_plus(os.getenv("DB_PASSWORD"))
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    DATABASE_URL = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'

