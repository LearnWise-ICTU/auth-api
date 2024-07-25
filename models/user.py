from beanie import Document, Indexed
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from typing import Annotated


from config.security import hash_password, is_strong_password


@dataclass
class UserName(BaseModel):
    first_name: str
    last_name: str
    nickname: Optional[str] = ""


class User(Document):
    name: UserName
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str
    is_active: bool = True
    verified_at: str | None = None
    updated_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    @property
    def full_name(self):
        return f"{self.name.first_name} {self.name.last_name}"
    

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.updated_at}".strip()


class CreateUser(BaseModel):
    name: UserName
    email: EmailStr
    password: str

    model_config = ConfigDict(
        extra="ignore",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": {
                    "first_name": "john",
                    "last_name": "doe",
                    "nickname": "johnny",
                },
                "email": "john@example.com",
                "password": "password",
            }
        },
    )

    @field_validator("password")
    def hash_password(cls, v):
        if not is_strong_password(v):
            raise ValueError(
                "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
            )
        return hash_password(v)
