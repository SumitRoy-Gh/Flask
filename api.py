###put and delete - HTTP Verbs
###Working with APIs -- JSON
###RESTful APIs

from flask import Flask, jsonify,request
app = Flask(__name__)
##initial data in my to do list
items=[{"id":1,"task":"python","completed":False},
      {"id":2,"task":"Flask","completed":False}]

@app.route('/')
def home():
    return "Welcome to the sample to do list app"

#Get: Retrive all the items
@app.route('/items',methods=["GET"])
def getitems():
    return jsonify(items)

##get: Retrieve specific items by id
@app.route('/items/<int:item_id>',methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    return jsonify(item)


##Post:Add New Item to List - API
@app.route('/items',methods=["POST"])
def add_item():
    if not request.json or not 'task' in request.json:
        return jsonify({"message": "Invalid request"}), 400
    new_item = {
        "id": len(items)+1,
        "task": request.json["task"],
        "completed": False
    }
    items.append(new_item)
    return jsonify({"message": "Item added successfully"}), 201


##Put:Update an existing item
@app.route('/items/<int:item_id>',methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    if not request.json or not 'task' in request.json:
        return jsonify({"message": "Invalid request"}), 400
    item["task"] = request.json["task"]
    item["completed"] = request.json.get("completed", item["completed"])
    return jsonify({"message": "Item updated successfully"}), 200


##Delete:Delete an item
@app.route('/items/<int:item_id>',methods=["DELETE"])
def delete_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    items.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200    

if __name__ == "__main__":
    app.run(debug=True)