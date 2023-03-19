import datetime

import psutil as psutil
from flask import Flask

app = Flask(__name__)


@app.route("/uptime/", methods=["GET"])
def uptime():
    uptime = psutil.boot_time()
    return f"Current time is {datetime.datetime.fromtimestamp(uptime)}"


if __name__ == "__main__":
    app.run(debug=True)
