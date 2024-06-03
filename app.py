from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", decode_responses=True)


@app.route("/")
def hello_world():
    redis.incr("views")
    counter = str(redis.get("views"))
    return f"<h1>This page has been viewed {counter} times!</h1>"
