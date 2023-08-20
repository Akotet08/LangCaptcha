from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.model import first
# from app.get_model import get_model


router = APIRouter(prefix="/auth")

@router.post("/{text_id}")
def get_translation_score(text_id: int, mt: str = Body(...), db: Session = Depends(get_db)):
    query = db.query(first).filter(first.id == text_id)
    result = db.execute(query).first()
    if not result:
        return {"error": "text not found"}
    
    src = result.en
    ref = result.ko
    user_input = mt

    # model = get_model_instance()
    # prediction = model.predict([{ "src": src, "ref": ref, "mt": user_input}], gpus=0, batch_size=8)
    
    input_src = tokenizer(src, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
    input_mt = tokenizer(user_input, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
    input_ref = tokenizer(ref, return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')

    inp = {"src_input_ids": input_src['input_ids'],
        "src_attention_mask": input_src['attention_mask'],
        "mt_input_ids": input_mt['input_ids'],
        "mt_attention_mask": input_mt['attention_mask'], 
        "ref_input_ids": input_ref['input_ids'],
        "ref_attention_mask": input_ref['attention_mask']}

    outputs = ort_sess.run(None, inp)

    return {"score": outputs}
