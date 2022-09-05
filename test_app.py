import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_json_with_proper_mimetype(client):
    # let's make sure responses are application/json
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_not_found(client):
    # let's make sure general not found errors work
    response = client.get('/not/real/url')
    json = response.get_json()
    assert response.status_code == 404
    assert response.content_type == 'application/json'
    assert json['error'] == '404 Not Found'


def test_hello_world(client):
    # let's test that we have a successful request
    # and that we're getting the JSON message
    response = client.get('/')
    json = response.get_json()
    assert json['message'] == 'Hello world!'


def test_lists(client):
    # let's make sure we get 2 lists back
    response = client.get('/lists')
    json = response.get_json()
    assert len(json['lists']) == 2


def test_single_list(client):
    # let's make sure we get a single list
    response = client.get('/lists/1')
    json = response.get_json()
    assert json['list']['name'] == 'This is an example list'


def test_single_list_items(client):
    # make sure that the list items are there
    response = client.get('/lists/1')
    json = response.get_json()
    assert len(json['list']['list_items']) == 3


def test_list_not_found(client):
    # make sure the error and response code are correct
    # when no list is found
    response = client.get('/lists/99')
    json = response.get_json()
    assert response.status_code == 404
    assert json['error'] == '404 Not Found'
