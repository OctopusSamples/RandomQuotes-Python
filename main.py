from flask import Flask, send_from_directory
from random import randint
from os import getenv

app = Flask(__name__)


@app.route("/api/quote")
def index():
    with open('quotes.txt') as f:
        quotes = [line.rstrip() for line in f]
    with open('authors.txt') as f:
        authors = [line.rstrip() for line in f]
    random_index = randint(0, len(quotes))
    return "{\"quote\": \"" + quotes[random_index] + "\", " \
        "\"author\": \"" + authors[random_index] + "\", " \
        "\"appVersion\": \"1.0.0\", " \
        "\"environmentName\": \"" + getenv('ENVIRONMENT_NAME', 'Local') + "\" " \
        "}"


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('public', path)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)