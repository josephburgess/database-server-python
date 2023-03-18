from flask import Blueprint

from ..controllers.get_controller import get_key_value

get_router = Blueprint('get_router', __name__)


@get_router.route('/get')
def get():
    return get_key_value()
