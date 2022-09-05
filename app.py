from flask import Flask, jsonify
from flask_restful import Resource, Api, abort

from mock_data import lists, list_items

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello world!'}


api.add_resource(HelloWorld, '/')


class GetLists(Resource):
    def get(self):
        return {'lists': lists}


api.add_resource(GetLists, '/lists')


class GetList(Resource):
    def get(self, list_id):
        _list = {}
        search = [_list for _list in lists if _list['id'] == list_id]
        if len(search) > 0:
            _list = search[0]
        else:
            abort(404, error='404 Not Found')
        _items = [_item for _item in list_items if _item['list_id'] == list_id]
        if len(_items) > 0:
            _list['list_items'] = _items
        return {'list': _list}


api.add_resource(GetList, '/lists/<int:list_id>')


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '404 Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
