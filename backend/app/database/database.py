from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connection details
DATABASE_URL = "postgresql://postgres:bytes@db:5432/bytes"

engine = create_engine(DATABASE_URL)

# SQLAlchemy session
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
