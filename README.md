# Small Items Flask App

## Installation and Environment

- `py -m venv .venv` to create a virtual environment.
- `source .venv/Scripts/activate` to start the environment.
- `py -m pip install requirements.txt` to get requirements/dependencies.
- `flask run` to start the server.

## Usage

Available routes:

- "GET":
  - "/" : Returns a .json list of routes.
  - "/items" : Returns a .json list of items
  - "/hello" : Returns .json Hello world.

- "POST":
  - "/items?search=%QUERY%" : Searches the names of items for %QUERY%, returning a matching list as .json.

To get data from a route, use Postman to create a request at http://localhost:5000 with whichever route and methods.
