import sqlite3

request_to_check_ivan_sovin_salary = """
SELECT salary FROM table_effective_manager WHERE name = "Иван Совин"
"""

request_most_effective = """
SELECT salary FROM table_effective_manager WHERE name = ?
"""

request_dismissal = """
DELETE FROM table_effective_manager WHERE name = ?
"""

request_increase = """
UPDATE table_effective_manager SET salary = salary * 1.1 WHERE name = ?
"""


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    salary_of_ivan = cursor.execute(request_to_check_ivan_sovin_salary).fetchone()[0]

    try:
        result = c.execute(request_most_effective, (name,)).fetchone()[0] * 1.1
    except TypeError:
        print(f"Сотрудник с данными {name} не найден")
        return

    if name == "Иван Совин":
        print("Нельзя изменить з/п эффективного менджера")
    elif result > salary_of_ivan:
        c.execute(request_dismissal, (name,))
        print(f"Сотрудник {name} уволен")
    elif result <= salary_of_ivan:
        c.execute(request_increase, (name,))
        print(f"з/п сотрудника {name} повышена!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        name = input("Введите имя сотрудника: ")
        ivan_sovin_the_most_effective(cursor, name)
