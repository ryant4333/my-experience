from sqlalchemy import create_engine, text, insert

import time

time.sleep(5)


postgresql_url = "postgresql://ryan:4123@postgres_db_container:5432/mydb"

engine = create_engine(postgresql_url)

conn = engine.connect()
query = text(
    "INSERT INTO projects (project_name, summary, details, tags, start_date, end_date) VALUES ('Experience Portal', 'The page you are on!', 'Detailed summary', NULL, '2025-01-10', '2025-03-01');"
)
conn.execute(query)
conn.commit()

print("done")


conn.close()
