from app.models import Person
from app.db import SessionLocal
from typing import List, Dict

class PersonService:
    @staticmethod
    def create(person_data: Dict) -> Person:
        db = SessionLocal()
        new_person = Person(
            first_name=person_data["first_name"],
            last_name=person_data["last_name"],
            company_name=person_data["company_name"],
        )
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
        db.close()
        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        db = SessionLocal()
        person = db.query(Person).get(person_id)
        db.close()
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        db = SessionLocal()
        people = db.query(Person).all()
        db.close()
        return people
