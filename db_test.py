import mariadb
import sys
try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3306,
        database="stock"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


cur.execute('''
CREATE TABLE records
 (boardnames text,
  popularity int,
  timestamp datetime)
''')

conn.commit()