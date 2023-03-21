import subprocess

from flask import Flask, Response
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class CorrectData(FlaskForm):
    code = StringField(validators=[InputRequired()])
    time = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])


@app.route("/distance_coding", methods=["POST"])
def check_the_code():
    form = CorrectData()

    if form.validate():
        if "shell=True" in form.code.data:
            return Response("Received insecure code", status=400)
        try:
            proc = subprocess.Popen(['python', '-c', form.code.data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outs, errs = proc.communicate(timeout=form.time.data)

            if errs:
                return Response(errs.decode(), status=400)
            else:
                return Response(outs.decode(), status=200)
        except subprocess.TimeoutExpired:
            proc.kill()
            return Response("Code execution time exceeds the time limit", status=400)
    else:
        return Response("Incorrect data entered", status=400)


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
