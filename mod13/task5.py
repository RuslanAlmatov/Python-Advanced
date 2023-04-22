import sqlite3
from random import random

data = [
    ("4", "Ливерпуль", "Англия", "Сильная"),
    ("2", "Бавария", "Германия", "Сильная"),
    ("3", "Челси", "Англия", "Сильная"),
    ("8", "Ювентус", "Италия", "Средняя"),
    ("6", "ПСЖ", "Франция", "Средняя"),
    ("12", "Аякс", "Нидерланды", "Средняя"),
    ("1", "Ман Сити", "Англия", "Сильная"),
    ("5", "Реал", "Испания", "Средняя"),
    ("7", "Манчестер Юнайтед", "Англия", "Средняя"),
    ("10", "Рома", "Италия", "Средняя"),
    ("13", "Боруссия Д", "Германия", "Средняя"),
    ("9", "Барселона", "Испания", "Средняя"),
    ("21", "Тотэнхем", "Англия", "Слабая"),
    ("16", "Лейпциг", "Германия", "Слабая"),
    ("23", "Арсенал", "Англия", "Слабая")
]


def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    c.executemany("INSERT INTO uefa_commands VALUES (?, ?, ?, ?)", data)
    groups = [[] for _ in range(number_of_groups)]
    strong_teams = [team for team in data if team[3] == "Сильная"]
    medium_teams = [team for team in data if team[3] == "Средняя"]
    weak_teams = [team for team in data if team[3] == "Слабая"]
    for i in range(number_of_groups):
        groups[i].append(random.choice(strong_teams))
        strong_teams.remove(groups[i][-1])
        groups[i].extend(random.sample(medium_teams, 2))
        medium_teams.remove(groups[i][-1])
        medium_teams.remove(groups[i][-2])
        groups[i].append(random.choice(weak_teams))
        weak_teams.remove(groups[i][-1])
        random.shuffle(groups[i])

    draw = [(team[0], i + 1) for i, group in enumerate(groups) for team in group]
    cursor.executemany("INSERT INTO uefa_draw (command_number, group_number) VALUES (?, ?)", draw)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        quantity_of_commands = int(input("Введите количество групп (от 4 до 16): "))
        generate_test_data(cursor, quantity_of_commands)
