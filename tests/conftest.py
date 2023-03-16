import pytest
from app import mongo, create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    with app.app_context():
        mongo.db.key_value_pairs.insert_one({'_id': 'test', 'value': 'value'})
    yield client
    with app.app_context():
        mongo.db.key_value_pairs.delete_one({'_id': 'test'})
