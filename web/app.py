from sqlalchemy import create_engine, text, insert

import time

time.sleep(5)


postgresql_url = "postgresql://ryan:4123@postgres_db_container:5432/mydb"

engine = create_engine(postgresql_url)

conn = engine.connect()
query = text(
    "INSERT INTO identity (_name, surname) VALUES ('Michel', 'Palefrois'), ('Renaud', 'Bertop');"
)
conn.execute(query)
conn.commit()

print("done")


conn.close()
