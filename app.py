from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Automated Testing Framework Demo!"

# In-memory "database"
items = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    items.append(data["name"])
    return jsonify({"message": "Item added", "items": items}), 201

if __name__ == "__main__":
    app.run(debug=True)
