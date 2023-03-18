from flask import request, jsonify
from ..app import mongo


def set_key_value():
    key = request.args.get('key')
    value = request.args.get('value')
    if key is None or value is None:
        return jsonify({'message': 'Bad request'}), 400
    result = mongo.db.key_value_pairs.update_one(
        {'_id': key}, {'$set': {'value': value}}, upsert=True)
    if result.upserted_id is None:
        return jsonify({'message': 'Created'}), 201
