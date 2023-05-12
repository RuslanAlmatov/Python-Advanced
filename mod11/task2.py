import logging
import threading
import time

import requests
import sqlite3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://swapi.dev/api/people/"
OUT_PATH = "mod21/star_wars.sqlite"
query = """
CREATE TABLE IF NOT EXISTS star_wars
(id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INTEGER)
"""


def get_persons(url: str, count: int):
    with sqlite3.connect("star_wars.sqlite") as conn:
        cursor = conn.cursor()

        response = requests.get(url + f"{count}/")
        if response.status_code == 200:
            data = response.json()
            name = data["name"]
            gender = data["gender"]
            birth_year = data["birth_year"]
            if birth_year == "unknown":
                age = 999999
            else:
                age = int(birth_year[:2])
            cursor.execute("INSERT INTO star_wars (name, gender, age) VALUES (?,?,?)", (name, gender, age))


def get_time_usually():
    start_time = time.time()
    for i in range(1, 22):
        get_persons(URL, i)
    end_time = time.time()
    print(f"Время работы обычной программы = {end_time - start_time}")


def get_time_multithreading():
    start_time = time.time()
    for i in range(22):
        thread = threading.Thread(target=get_persons, args=(URL, i))
        thread.start()

    end_time = time.time()
    print(f"Время работы программы с потоками = {end_time - start_time}")


if __name__ == "__main__":
    with sqlite3.connect("star_wars.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(query)
    get_time_usually()
    get_time_multithreading()
