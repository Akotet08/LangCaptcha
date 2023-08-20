from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import random

from app.database.database import get_db
from app.database.model import first, prompt, second

router = APIRouter(prefix="/api")

@router.get("/first")
def show_first_prompt(db: Session = Depends(get_db)):
    query = first.select()
    result = db.execute(query).all()
    chosen_prompt = random.choice(result)
    return {"prompt_id": chosen_prompt.id, "prompt_text": chosen_prompt.en}

@router.get("/second")
def show_second_prompt(db: Session = Depends(get_db)):
    query = prompt.select()
    result = db.execute(query).all()
    chosen_prompt = random.choice(result)
    return {"prompt_id": chosen_prompt.id, "prompt_text": chosen_prompt.text}

@router.post("/second")
def save_translation(answer: dict, db: Session = Depends(get_db)):
    query = second.insert().values(**answer)
    db.execute(query)
    db.commit()
    return {"message": "successfully inserted translation entry"}
