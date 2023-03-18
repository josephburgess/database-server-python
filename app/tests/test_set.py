import json
import pytest

from app import mongo


@pytest.fixture(scope='module')
def clear_test_db():
    mongo.db.key_value_pairs.delete_many({})


def test_set_with_valid_data(client, clear_test_db):
    response = client.put('/set?key=test&value=value')
    assert response.status_code == 201
    assert json.loads(response.data) == {'message': 'Created'}


def test_set_with_no_data(client, clear_test_db):
    response = client.put('/set')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': 'Bad request'}


def test_set_with_invalid_data(client, clear_test_db):
    response = client.put('/set?key=test')
    assert response.status_code == 400
    assert json.loads(response.data) == {'message': 'Bad request'}
