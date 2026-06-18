# Small Items Flask App

## Installation and Environment

- `py -m venv .venv` to create a virtual environment.
- `source .venv/Scripts/activate` to start the environment.
- `py -m pip install requirements.txt` to get requirements/dependencies.
- `flask run` to start the server.

## Usage

items.json is included with basic examples and seed data.
Available routes:

- "GET":
  - "/" : Returns a .json list of routes.
  - "/items" : Returns a .json list of items
  - "/hello" : Returns .json Hello world.
  - "/items/search?name=%QUERY%" : Searches the names of items for %QUERY%, returning a matching list as .json.

- "POST":
  - "/items/create" : Adds an item to the list of items, and returns the created item.

  Header: `"Content-Type: application/json"`

  Json example:

  ```json
    {
        "name": "name",
        "value": 0,
        "type": "armor" | "weapon" | "consumable"
    }
  ```

To get data from a route, use Postman to create a request at http://localhost:5000 with whichever route and methods.
