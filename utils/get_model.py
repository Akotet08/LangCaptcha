from comet import download_model, load_from_checkpoint

def get_model():
    # Download model from HuggingFace
    model_path = download_model("Unbabel/wmt22-comet-da")
    model = load_from_checkpoint(model_path)

    return model

# Test flow
model = get_model()

user_input = '기사는'
ref = '이 기사는 2010년 9월 18일 글로벌 보이스에 이탈리아어로 먼저 게재되었습니다.'
src = 'This story was originally published on Global Voices in Italian on September 18, 2010'

prediction = model.predict([{ "src": src, "ref": ref, "mt": user_input}], gpus=0, batch_size=8)
print(prediction[0][0])