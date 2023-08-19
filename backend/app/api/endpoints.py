from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.model import second

router = APIRouter(prefix="/api")

@router.post("")
def add_translation(answer: dict, db: Session = Depends(get_db)):
    query = second.insert().values(**answer)
    db.execute(query)
    db.commit()
    return {"message": "successfully inserted translation entry"}
