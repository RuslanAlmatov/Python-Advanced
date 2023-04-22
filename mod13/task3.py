import datetime
import sqlite3

request_log_bird = """
INSERT INTO 'table_with_birds'(name,date_time) VALUES (?, ?)
"""

request_check_bird = """
SELECT EXISTS(SELECT 1 FROM 'table_with_birds' WHERE name = ? LIMIT 1)
"""


def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    c.execute(request_log_bird, (bird_name, date_time))


def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    result = c.execute(request_check_bird, (bird_name,)).fetchone()[0]
    return result


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS table_with_birds(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date_time TEXT NOT NULL);
        """)
        log_bird(cursor, name, right_now)

        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
