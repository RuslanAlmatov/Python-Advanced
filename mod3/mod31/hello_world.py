from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/hello-world/<string:name>")
def hello(name) -> str:
    weekday = datetime.today().weekday()
    weekdays_tuple = tuple(['Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
                            'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья'])
    if name in weekdays_tuple:
        raise ValueError("Вы ввели не имя")
    return f"Привет, {name}. {weekdays_tuple[weekday]}"
