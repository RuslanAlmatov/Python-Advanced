import shlex
import string
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps/", methods=["GET"])
def current_process():
    args: list[str] = request.args.getlist('arg')
    cleaned_args = [shlex.quote(i) for i in args]
    command_str = f"ps {' '.join(cleaned_args)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()
    return string.Template(f"ps <pre>${output}</pre>").substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
