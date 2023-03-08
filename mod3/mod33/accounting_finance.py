from datetime import datetime
from flask import Flask

app = Flask(__name__)

#  storage = {2022: {2: {18: 300, 20: 600}, 10: {17: 1000, 31: 500}},
#            2023: {1: {5: 700, 17: 12000}, 2: {16: 10000, 24: 900}}}
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
