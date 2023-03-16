from flask import Blueprint

from controllers.set_controller import set_key_value

set_router = Blueprint('set_router', __name__)


@set_router.route('/set', methods=['PUT'])
def put():
    return set_key_value()
