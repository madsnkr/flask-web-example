from flask import Flask
from redis import Redis

app = Flask(__name__)

app.config.from_prefixed_env("REDIS")
redis = Redis(host=app.config["HOST"], port=app.config["PORT"], decode_responses=True)


@app.route("/")
def hello_world():
    redis.incr("views")
    counter = str(redis.get("views"))
    return f"<h1>This page has been viewed {counter} times!</h1>"
