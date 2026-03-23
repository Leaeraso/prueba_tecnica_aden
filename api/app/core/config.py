from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "University API"
    debug: bool = False
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    expires_in: int = 3600
    student_number_start: int = 50000
    classroom_number_start: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()
