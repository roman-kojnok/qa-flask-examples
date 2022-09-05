from flask import Flask, Response
app = Flask(__name__)


@app.route('/get/text', methods=['GET'])
def get_text():
    return Response("Hello from the flask API", mimetype='text/plain')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    