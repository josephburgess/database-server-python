from app import create_app, mongo
import pytest


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    with app.app_context():
        mongo.db.key_value_pairs.insert_one({'_id': 'test', 'value': 'value'})
    yield client
    with app.app_context():
        mongo.db.key_value_pairs.delete_one({'_id': 'test'})


def pytest_configure(config):
    app = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase_test'
    with app.app_context():
        mongo.cx.drop_database('mydatabase_test')
        mongo.init_app(app)
