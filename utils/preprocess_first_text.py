import pandas as pd

from sqlalchemy import create_engine


engine = create_engine("postgresql://postgres:bytes@localhost:5432/bytes")

data_dict = {}

with open("../data/korean-english-park.dev/korean-english-park.dev.en") as f:
    data_dict["en"] = f.readlines()

with open("../data/korean-english-park.dev/korean-english-park.dev.ko") as f:
    data_dict["ko"] = f.readlines()

df = pd.DataFrame.from_dict(data_dict)
df.index += 1
df.to_sql(name="first", con=engine, if_exists="replace", index_label="id")
