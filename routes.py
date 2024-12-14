
from flask import Blueprint, jsonify, request

blueprint = Blueprint("api", __name__)

data = []  # Simulando base de datos en memoria

@blueprint.route('/items', methods=['GET'])
def get_items():
    return jsonify(data), 200

@blueprint.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in data if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@blueprint.route('/items', methods=['POST'])
def create_item():
    item = request.json
    data.append(item)
    return jsonify({"message": "Item created"}), 201

@blueprint.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in data if i["id"] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify({"message": "Item updated"}), 200
    return jsonify({"error": "Item not found"}), 404

@blueprint.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [i for i in data if i["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200
