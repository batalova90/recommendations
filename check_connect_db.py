import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()

conn = psycopg2.connect(
    host="127.0.0.1",
    database=os.getenv('NAME_DB'),
    user=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)


try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews_reviews;")
    for row in cursor.fetchall():
        print(row)
finally:
    conn.close()
