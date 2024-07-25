from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import List

from fastapi import BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from pathlib import Path
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", from_attributes=True, extra="ignore"
    )

    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str = ""
    MONGODB_URL: str
    DATABASE_NAME: str
    MAIL_USERNAME: str = "bhp6cxozu9n54awq"
    MAIL_PASSWORD: str = "70sbfbjn0oivqpti"
    MAIL_FROM: str = "noreply@test.com"
    MAIL_PORT: int = 2525
    MAIL_HOST: str = "smtp.mailmug.net"
    MAIL_SERVER: str
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool = True
    MAIL_FROM_NAME: str
    MAIL_DEBUG: bool
    MAILTRAP_TOKEN: str

    FRONTEND_HOST: str = "http://localhost:3000"
