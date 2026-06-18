from flask import Flask, request
from items import load_items, add_new_item

app = Flask(__name__)

@app.route("/items")
def items():
    return load_items()

@app.route("/hello")
def hello():
    return {"Hello": "World!"}

@app.route("/")
def home():
    return {"Instead try:": [{"GET":"/items"}, {"GET":"/hello"}, {"GET": "/items/search?=%SEARCH_TERM%"}, {"POST": "/items/create"}]}

@app.route("/items/search")
def search():
    search_name = request.args.get("name", '')
    search_res = []
    for item in load_items():
        if search_name.lower() in item["name"].lower():
            search_res.append(item)
    
    if len(search_res) > 0:
        return search_res
    
    return f"Not found, searching for {search_name}"
    
@app.post("/items/create")
def add_item():
    item = request.json
    if "name" not in item and "value" not in item and "type" not in item:
        # stretch: add validation for each value
        item_added = add_new_item(item)
        return f"{item_added["name"]} created!", 201
    return {"message": "Incorrect json format."}, 415

