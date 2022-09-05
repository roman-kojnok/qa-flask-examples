from flask import Flask, Response, request
app = Flask(__name__)

dictionary = {'key1': 'value1', 'key2': 'value2'}


@app.route('/')
def home():
    return dictionary


@app.route('/<string:key>', methods=['PUT'])
def update(key):
    dictionary[key] = request.data.decode('utf-8')
    return Response(key + " changed to: " + request.data.decode('utf-8'))
