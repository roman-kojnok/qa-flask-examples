from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.get_json()
    data_returned = "The data you send: " + data_sent
    return jsonify({'data': data_returned})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
