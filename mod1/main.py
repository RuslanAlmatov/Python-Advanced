import datetime
import os.path
import random
import re

from flask import Flask

app = Flask(__name__)
brandOfCar = ["Chevrolet", "Renault", "Ford", "Lada"]
breedOfCat = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
count = 0

@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"

@app.route("/cars")
def cars():
    global brandOfCar
    return (", ".join(brandOfCar))

@app.route("/cats")
def cats():
    global breedOfCat
    return random.choice(breedOfCat)

@app.route("/get_time/now")
def time_now():
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"

@app.route("/get_time/feature")
def time_feature():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет: {current_time_after_hour}"

@app.route("/get_random_word")
def get_word():
    with open(BOOK_FILE, encoding="UTF-8") as book:
        data = book.read()
        arr = re.split(r'[;,.\s]', data)
        return random.choice(arr)

@app.route("/counter")
def counter():
    global count
    count +=1
    return f"Количество посещений: {count}"

if __name__ == "__main__":
    app.debug = True
    app.run()