import uuid
from sqlalchemy.orm import Session
from app.model.personDetails import PersonDetails
from app.DTO.personDataDTO import PersonCreate


def create_person_service(person_data: PersonCreate, db: Session):
    # Check for duplicates
    existing_user = db.query(PersonDetails).filter(
        (PersonDetails.email == person_data.email) |
        (PersonDetails.username == person_data.username)
    ).first()

    if existing_user:
        raise ValueError("Email or Username already exists")

    # Create new person
    new_person = PersonDetails(
        bookifyid=str(uuid.uuid4()),
        firstname=person_data.firstname,
        lastname=person_data.lastname,
        phonenumber=person_data.phonenumber,
        email=person_data.email,
        username=person_data.username,
        password=person_data.password,  # hash later
        street=person_data.street or "",
        apartment=person_data.apartment,
        city=person_data.city,
        state=person_data.state,
        zipcode=person_data.zipcode,
        county=person_data.county,
        role=person_data.role
    )

    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person
