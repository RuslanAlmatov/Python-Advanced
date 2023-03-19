import shlex

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps/", methods=["GET"])
def current_process():
    args: list[str] = request.args.getlist('arg')
    cleaned_args = [shlex.quote(i) for i in args]
    return f"ps <pre>{''.join(cleaned_args)}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
