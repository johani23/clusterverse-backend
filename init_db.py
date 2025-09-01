from database import get_db_connection

with open('schema.sql') as f:
    conn = get_db_connection()
    conn.executescript(f.read())
    conn.commit()
    conn.close()