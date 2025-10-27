from pydantic import BaseModel, Field

from app.DTO.personDataDTO import PersonBase


class LoginPerson(BaseModel):
    username: str = Field(..., min_length=6, max_length=12)
    password: str = Field(..., min_length=6, max_length=12)

class LoginResponse(PersonBase):
    bookifyid: str  # use your table primary key

    model_config={
        "form_attributes" : True
    }
