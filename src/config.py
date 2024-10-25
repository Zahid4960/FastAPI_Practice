from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str ="postgresql+asyncpg://postgres:%21%40%23DreamOnline123@localhost:5432/bookly_dev_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
Config = Settings()
