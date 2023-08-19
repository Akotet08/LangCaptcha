import sys

sys.path.append(sys.path[0] + '/..')

from backend.app.database.model import metadata

from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:bytes@localhost:5432/bytes")
metadata.create_all(bind=engine)

insert_stmt = text("""DELETE FROM prompt;

INSERT INTO prompt (text)
VALUES
    ('I cannot find my umbrella.'),
    ('Where is the organizer of this event'),
    ('There should be a policy that limits the number of visitors in the school per day.')
;
""")

with engine.connect() as conn:
    conn.execute(insert_stmt)
    conn.commit()
