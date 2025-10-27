from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.DTO.personDataDTO import PersonCreate, PersonResponse
from app.service.personDetailsService import create_person_service

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
