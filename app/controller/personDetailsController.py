from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.DTO.loginDTO import LoginPerson, LoginResponse
from app.db.session import SessionLocal
from app.DTO.personDataDTO import PersonCreate, PersonResponse
from app.service.personDetailsService import create_person_service, login_person_service

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
def create_person(person_data: PersonCreate, db: Session = Depends(get_db)):
    try:
        new_person = create_person_service(person_data, db)
        return new_person
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login_person(person_data: LoginPerson, db: Session = Depends(get_db)):
    try:
        response_data = login_person_service(person_data, db)
        return response_data
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

