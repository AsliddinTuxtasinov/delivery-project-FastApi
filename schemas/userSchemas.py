from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        # schema_extra -> optional
        schema_extra = {
            "example": {
                "username": "asliddin_1010",
                "email": "asliddintukhtasinov5@gmail.com",
                "password": "password1!",
                "is_staff": False,
                "is_active": True
            }
        }
