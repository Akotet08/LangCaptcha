from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

# Define tables

first = Table(
    "first", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("en", String),
    Column("ko", String)
)

prompt = Table(
    "prompt", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("text", String)
)

second = Table(
    "second", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("prompt_id", Integer, ForeignKey("prompt.id")),
    Column("translation", String)
)
