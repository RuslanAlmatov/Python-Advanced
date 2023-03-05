import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)
BASE_DIR_1 = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR_1, "output_file.txt")
BASE_DIR_2 = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR_2, 'simple.txt')

def get_summary_rss():
    with open(FILE, encoding= "UTF-8") as file:
        data = file.readlines()[1:]
        sum = 0
        for i in data:
            columns = i.split()
            sum = sum + int(columns[5])
        return f"Сумма равна: {sum} байт, {round(sum / 2**10, 2)} килобайт, {round(sum / 2**20, 2)} мегабайт"

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
    print(storage.setdefault(year, {}).setdefault(month, {}))
    print(storage.setdefault(month, {}).setdefault(day, {}))
    print(storage)
    return  f"{number}"

if __name__ == "__main__":
    app.run(debug=True)
