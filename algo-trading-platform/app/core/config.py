from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    redis_host: str = "localhost"
    redis_port: int = 6379

    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    @property
    def database_url(self) -> str:
        encoded_password = quote(self.db_password, safe="")
        return (
            f"postgresql+asyncpg://"
            f"{self.db_username}:{encoded_password}"
            f"@{self.db_host}:{self.db_port}"
            f"/{self.db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
