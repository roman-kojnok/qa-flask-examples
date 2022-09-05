from flask import jsonify, Flask
import json

appFlask = Flask(__name__)

dict = {'username': 'eduCBA', 'account': 'Premium', 'validity': '2709 days'}


@appFlask.route('/home_jsonify')
def home_jsonify():
    # dict = {'username': 'eduCBA', 'account': 'Premium', 'validity': '2709 days'}
    return jsonify(dict)


@appFlask.route('/home_dumps')
def home_dumps():
    # dict = {'username': 'eduCBA', 'account': 'Premium', 'validity': '2709 days'}
    return json.dumps(dict)


if __name__ == "__main__":
    appFlask.run(debug=True)
