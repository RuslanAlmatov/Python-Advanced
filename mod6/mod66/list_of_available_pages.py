import datetime
import os.path
import random
import re

from flask import Flask, url_for

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
    count += 1
    return f"Количество посещений: {count}"


@app.route("/hello-world/<string:name>")
def hello(name) -> str:
    weekday = datetime.today().weekday()
    weekdays_tuple = tuple(['Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
                            'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья'])
    return f"Привет, {name}. {weekdays_tuple[weekday]}"


@app.route("/max_number/<path:numbers>")
def getMaxNumber(numbers) -> str:
    arr = numbers.split("/")
    max = -1
    for i in arr:
        if not (i.isnumeric()):
            return "Вы ввели не число"
        elif int(i) > max:
            max = int(i)
    return f"Максимальное число: <i>{max}</i>"


@app.route("/<int:size>/<path:relative_path>")
def get_result(size, relative_path) -> str:
    with open(FILE, encoding="UTF-8") as file:
        abs_path = os.path.abspath(relative_path)
        file_readed = " ".join(file.read(size).rsplit())
        return f"<b>{abs_path}</b> {len(file_readed)} <br> {file_readed}"


storage = {}


@app.route("/add/<date>/<int:number>")
def add(date, number):
    global storage
    year, month, day = datetime.datetime.strptime(date, '%Y%m%d').year, \
                       datetime.datetime.strptime(date, '%Y%m%d').month, \
                       datetime.datetime.strptime(date, '%Y%m%d').day
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    return f"Информация о тратах на {year}-{month}-{day}: {storage[year][month][day]}"


@app.route("/calculate/<int:year>")
def calculate_year(year):
    sum = 0
    for key_y, key_m in storage[year].items():
        for key_d, value in key_m.items():
            sum += value
    return f"Сумма ваших затрат за {year} год: {sum}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_year_month(year, month):
    sum = 0
    for key, value in storage[year][month].items():
        sum += value
    return f"Ваши суммарные затраты за {year} год в {month}: {sum}"


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.errorhandler(404)
def handle_exception(err):
    list_of_links = ""
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((f"http://127.0.0.1:5000{url}", rule.endpoint))
        for link, name in links:
            list_of_links += f'</br><a href="{link}">{link}<a>'
    return list_of_links


if __name__ == "__main__":
    app.debug = True
    app.run()
