import json


def test_get_with_key_exists(client):
    response = client.get('/get?key=test')
    assert response.status_code == 200
    assert json.loads(response.data) == {'message': 'OK', 'value': 'value'}


def test_get_with_key_does_not_exist(client):
    response = client.get('/get?key=nonexistent')
    assert response.status_code == 404
    assert json.loads(response.data) == {
        'message': "Key 'nonexistent' not found"}


def test_get_with_no_key(client):
    response = client.get('/get')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': 'Bad request'}
