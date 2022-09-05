from flask import Flask, Response, request
app = Flask(__name__)

dictionary = {'key1': 'value1', 'key2': 'value2'}


@app.route('/')
def home():
    return dictionary


@app.route('/<string:key>', methods=['DELETE'])
def deleter(key):
    dictionary.pop(key)
    return Response(key + " deleted from dictionary")
