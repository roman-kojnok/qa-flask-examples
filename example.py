from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/temp')
def index2():
    return 'ajay rao'


if __name__ == '__main__':
    app.run(debug=True)
