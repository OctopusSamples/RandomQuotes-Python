from flask import Flask
from random import randint
from os import getenv

app = Flask(__name__)


@app.route("/api/quote")
def index():
    with open('quotes.txt') as f:
        quotes = [line.rstrip() for line in f]
    with open('authors.txt.txt') as f:
        authors = [line.rstrip() for line in f]
    random_index = randint(0, len(quotes))
    return "{\"quote\": \"" + quotes[random_index] + "\", " \
        "\"author\": \"" + authors[random_index] + "\", " \
        "\"appVersion\": \"1.0.0\", " \
        "\"environmentName\": \"" + getenv('ENVIRONMENT_NAME', 'Local') + "\" " \
        "}"
