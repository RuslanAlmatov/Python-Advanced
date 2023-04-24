import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

with open('create_schema.sql', 'r') as sql_file:
    sql_script: str = sql_file.read()

with sqlite3.connect('database.sqlite') as conn:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
