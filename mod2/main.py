import os
from datetime import datetime
from flask import Flask
import sys
from statistics import mean

app = Flask(__name__)
BASE_DIR_1 = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR_1, "output_file.txt")
BASE_DIR_2 = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR_2, 'simple.txt')


def get_summary_rss():
    with open(FILE, encoding="UTF-8") as file:
        data = file.readlines()[1:]
        sum = 0
        for i in data:
            columns = i.split()
            sum = sum + int(columns[5])
        return f"Сумма равна: {sum} байт, {round(sum / 2 ** 10, 2)} килобайт, {round(sum / 2 ** 20, 2)} мегабайт"


def get_mean_size():
    data = sys.stdin.readlines()[1:]
    arr = []
    for i in data:
        columns = i.split()
        arr.append(int(columns[4]))
    print(mean(arr))


def decrypt(letter: str):
    result = []

    for i in letter:
        result.append(i)
        if len(result) > 2 and (result[-1], result[-2]) == (".", "."):
            result.pop()
            result.pop()
            if result:
                result.pop()
    return "".join(i for i in result if i != ".")


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
    year, month, day = datetime.strptime(date, '%Y%m%d').year, \
                       datetime.strptime(date, '%Y%m%d').month, \
                       datetime.strptime(date, '%Y%m%d').day
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


if __name__ == "__main__":
    app.run(debug=True)
