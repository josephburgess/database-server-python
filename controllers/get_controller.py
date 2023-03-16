from app import mongo
from flask import current_app, jsonify, request


def get_key_value():
    with current_app.app_context():
        key = request.args.get('key')
        if key is None:
            return jsonify({'message': 'Bad request'}), 400
        result = mongo.db.key_value_pairs.find_one({'_id': key})
        if result is None:
            return jsonify({'message': f"Key '{key}' not found"}), 404
        return jsonify({'message': 'OK', 'value': result['value']}), 200
