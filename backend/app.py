from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()
app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask-tutorial']
todos_collection = db["todo"]





@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    # Extract fields
    name = form_data.get('username')
    email = form_data.get('email')

    return f"Success! Welcome {name}, your email {email} has been registered."

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data': data
    }
    return jsonify(data)
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    # Accept JSON or form
    data = request.get_json() or request.form

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"message": "itemName and itemDescription are required"}), 400

    todo_doc = {
        "itemName": item_name,
        "itemDescription": item_description,
    }

    result = todos_collection.insert_one(todo_doc)

    return jsonify({
        "message": "To-Do item stored successfully",
        "id": str(result.inserted_id)
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
