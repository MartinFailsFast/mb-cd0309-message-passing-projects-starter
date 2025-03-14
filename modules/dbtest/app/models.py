from sqlalchemy import Column, String, Integer
from app.db import Base

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    company_name = Column(String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_name": self.company_name,
        }