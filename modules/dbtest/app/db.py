from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://ct_admin:hotdogsfordinner@localhost:5432/geoconnections"
#DATABASE_URI = "postgresql://user:password@localhost:5432/mydatabase"


engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
This function provides a database session for use in dependency injection.
It ensures that the session is properly closed after use.
"""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    try:
        with engine.connect() as connection:
            print("✅ Successfully connected to the database!")
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")


if __name__ == "__main__":
    test_connection()