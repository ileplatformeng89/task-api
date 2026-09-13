from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str
    database_test_name: str = "tasks_test"
    database_user: str
    database_password_file: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def database_password(self) -> str:
        if self.database_password_file:
            return Path(self.database_password_file).read_text().strip()

        raise ValueError("DATABASE_PASSWORD_FILE is required")

    def build_database_url(self, database_name: str) -> URL:
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.database_user,
            password=self.database_password,
            host=self.database_host,
            port=self.database_port,
            database=database_name,
        )

    @property
    def database_url(self) -> URL:
        return self.build_database_url(self.database_name)

    @property
    def test_database_url(self) -> URL:
        return self.build_database_url(self.database_test_name)


settings = Settings()
