from flask import Flask, request
app = Flask(__name__)


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)


"""
http://127.0.0.1:5000/query?name=Pedro&location=UK
"""
