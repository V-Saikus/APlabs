from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/hello-world-23')
def var():
    return 'Hello World 23'

with make_server('', 5000, app) as server:
    print("Server srated")

    server.serve_forever()
