from pydantic import BaseModel, EmailStr, constr, field_validator, ConfigDict, model_validator
from typing import Optional
from datetime import datetime
from app.utils.validators import validate_password_strength

class UserCreateSchema(BaseModel):
    username: constr(strip_whitespace=True, min_length=3, max_length=50)
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        validate_password_strength(v)
        return v

class UserUpdateSchema(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    current_password: str
    username: Optional[constr(strip_whitespace=True, min_length=3, max_length=50)] = None
    new_password: Optional[str] = None

    @field_validator("current_password", "new_password")
    def validate_passwords(cls, v):
        if v is not None:
            validate_password_strength(v)
        return v

    @model_validator(mode='after')
    def check_passwords_differ(self):
        if self.new_password is not None and self.new_password == self.current_password:
            raise ValueError("New password must be different from the current password")
        return self

class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime
