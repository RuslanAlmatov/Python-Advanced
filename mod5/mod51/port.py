import subprocess
import shlex

from flask import Flask

app = Flask(__name__)


def run_server(port):
    request = shlex.split(f'lsof -i:{port}')
    res = subprocess.run(request, capture_output=True, text=True)
    if res.stdout.strip() != '':
        pid = res.stdout.strip()
        request = shlex.split(f'kill {pid}')
        subprocess.run(request)
    app.run(port=port)


if __name__ == '__main__':
    run_server(5000)
