import os, sys
from transformers import AutoTokenizer
import torch
from comet import download_model, load_from_checkpoint
import onnxruntime as ort


CONVERTED_COMET_DIR = 'CONVERTED_COMET'
CONVERTED_COMET_MODEL_PATH = os.path.join(CONVERTED_COMET_DIR, 'model.onnx')
tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-large')
MODEL_MAX_LENGTH = tokenizer.model_max_length

try: 
    os.makedirs(CONVERTED_COMET_DIR)
except FileExistsError:
    sys.exit(0)

input_names = ["src_input_ids", "src_attention_mask", "mt_input_ids", "mt_attention_mask", "ref_input_ids", "ref_attention_mask"]
inputs = {key: torch.ones(1, MODEL_MAX_LENGTH, dtype=torch.int64) for key in input_names}
symbolic_names = {0: "batch_size"}

model = load_from_checkpoint(download_model("Unbabel/wmt22-comet-da"))

torch.onnx.export(
    model,
    (*[inputs[key] for key in input_names],),
    CONVERTED_COMET_MODEL_PATH,
    opset_version=15,
    do_constant_folding=True,
    input_names=input_names,
    output_names=["score"],
    dynamic_axes={key: symbolic_names for key in input_names},
)


# Test
# onnx.checker.check_model(CONVERTED_COMET_MODEL_PATH)
ort_sess = ort.InferenceSession(CONVERTED_COMET_MODEL_PATH)

input_src = tokenizer("This story was originally published on Global Voices in Italian on September 18, 2010", return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
input_mt = tokenizer("이 기사는 2010년 9월 18일 글로벌 보이스에 이탈리아어로 먼저 게재되었습니다.", return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')
input_ref = tokenizer("이 기사는 2010년 9월 18일 글로벌 보이스에 이탈리아어로 먼저 게재되었습니다.", return_tensors="np", max_length=MODEL_MAX_LENGTH, padding='max_length')

inp = {"src_input_ids": input_src['input_ids'],
       "src_attention_mask": input_src['attention_mask'],
       "mt_input_ids": input_mt['input_ids'],
       "mt_attention_mask": input_mt['attention_mask'], 
       "ref_input_ids": input_ref['input_ids'],
       "ref_attention_mask": input_ref['attention_mask']}

outputs = ort_sess.run(None, inp)
print(outputs)