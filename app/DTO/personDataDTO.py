from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from app.model import roleEnum
from app.model.roleEnum import RoleEnum


### Base DTO ###
class PersonBase(BaseModel):
    firstname: str = Field(..., max_length=100)
    lastname: str = Field(..., max_length=100)
    phonenumber: str
    email: EmailStr
    street: str | None = None
    city: str | None = None
    state: str | None = None
    city: str | None = None
    state: str | None = None
    zipcode: str | None = None
    apartment: str | None = None
    county: str | None = None
    role: Optional[RoleEnum] = RoleEnum.user

### For creating a new person ###
class PersonCreate(PersonBase):
    username: str = Field(..., min_length=6, max_length=12)
    password: str = Field(..., min_length=6, max_length=12)

### Response schema ###
class PersonResponse(PersonBase):
    bookifyid: str  # use your table primary key

    model_config={
        "form_attributes" : True
    }
