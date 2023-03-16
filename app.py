from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
    mongo.init_app(app)

    from routes.get_router import get_router
    from routes.set_router import set_router

    app.register_blueprint(get_router)
    app.register_blueprint(set_router)
    return app
