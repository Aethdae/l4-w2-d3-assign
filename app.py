from flask import Flask, request
from items import load_items

app = Flask(__name__)

@app.route("/items")
def items():
    return load_items()

@app.route("/hello")
def hello():
    return {"Hello": "World!"}

@app.route("/")
def home():
    return {"Instead try:": [{"GET":"/items"}, {"GET":"/hello"}, {"POST": "/items?search=%SEARCH_TERM%"}]}

@app.post("/items")
def search():
    if request.method == 'POST':
        search_term = request.args.get("search")
        search_res = []
        for item in load_items():
            if search_term in item["name"].lower():
                search_res.append(item)
        
        if len(search_res) > 0:
            return search_res
        
        return f"Not found, searching for {search_term}"
