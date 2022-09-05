from flask import Flask, Response, request
app = Flask(__name__)


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("This is the data you sent to the API: " + data_sent, mimetype='text/plain')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    