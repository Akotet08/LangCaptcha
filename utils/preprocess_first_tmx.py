import pandas as pd

from sqlalchemy import create_engine
from translate.storage.tmx import tmxfile


engine = create_engine("postgresql://postgres:bytes@localhost:5432/bytes")

with open("../data/en-ko-handpicked.tmx", 'rb') as fin:
    tmx_file = tmxfile(fin, 'en', 'ko')

data_dict = {"en": [], "ko": []}


for node in tmx_file.unit_iter():
    data_dict["en"].append(node.source)
    data_dict["ko"].append(node.target)

df = pd.DataFrame.from_dict(data_dict)
df.index += 1
df.to_sql(name="first", con=engine, if_exists="replace", index_label="id")
