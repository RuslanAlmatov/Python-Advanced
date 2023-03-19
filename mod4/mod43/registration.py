from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Введите email"), Email(message="Введите корректный email")])
    phone = IntegerField(validators=[InputRequired(message="Введите номер телефона"), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired(message="Введите имя")])
    address = StringField(validators=[InputRequired(message="Введите адрес")])
    index = IntegerField(validators=[InputRequired(message="Введите индекс")])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Succssesfuly registred user {email} with phone +7{phone}"
    return f"invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
