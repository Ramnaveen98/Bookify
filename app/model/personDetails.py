from app.db.base import Base
from sqlalchemy import Column, String, Enum as SQLEnum

from app.model import roleEnum
from app.model.roleEnum import RoleEnum


class PersonDetails(Base):
    __tablename__ = "person_details"

    bookifyid = Column(String(30), primary_key=True, index=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    phonenumber = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

    # Address fields
    street = Column(String(50), nullable=False)
    apartment = Column(String(50), nullable=True)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    zipcode = Column(String(20), nullable=False)
    county = Column(String(100), nullable=False)

    role = Column(SQLEnum(RoleEnum), default=RoleEnum.user, nullable=False)
