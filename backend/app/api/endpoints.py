from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from transformers import AutoTokenizer

import onnxruntime as ort
import os
import random

from app.database.database import get_db
from app.database.model import first, prompt, second

router = APIRouter(prefix="/api")

CONVERTED_COMET_DIR = 'app/CONVERTED_COMET'
CONVERTED_COMET_MODEL_PATH = os.path.join(CONVERTED_COMET_DIR, 'model.onnx')

ort_sess = ort.InferenceSession(CONVERTED_COMET_MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-large')

@router.get("/first")
def show_first_prompt(db: Session = Depends(get_db)):
    query = first.select()
    result = db.execute(query).all()
    chosen_prompt = random.choice(result)
    return {"prompt_id": chosen_prompt.id, "prompt_text": chosen_prompt.en}

@router.post("/first")
def get_translation_score(answer: dict, db: Session = Depends(get_db)):
    MODEL_MAX_LENGTH = tokenizer.model_max_length

    query = db.query(first).where(first.c.id == answer["prompt_id"])
    result = db.execute(query).first()
    if not result:
        return {"error": "text not found"}
    
    src = result.en
    ref = result.ko
    user_input = answer["translation"]
    
    input_src = tokenizer(src, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
    input_mt = tokenizer(user_input, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
    input_ref = tokenizer(ref, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')

    inp = {"src_input_ids": input_src['input_ids'],
        "src_attention_mask": input_src['attention_mask'],
        "mt_input_ids": input_mt['input_ids'],
        "mt_attention_mask": input_mt['attention_mask'], 
        "ref_input_ids": input_ref['input_ids'],
        "ref_attention_mask": input_ref['attention_mask']}

    outputs = ort_sess.run(None, inp)[0][0].item()

    return {"score": outputs}

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
