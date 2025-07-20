# src/my_app/config.py
import os
from pydantic import BaseSettings, ConfigDict

PROD = "production"


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=None if os.getenv("ENVIRONMENT") == PROD else ".env",
        frozen=True,
        extra="forbid",
        validate_assignment=True,
    )


settings = Settings()
