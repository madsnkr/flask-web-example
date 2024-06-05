from flask import Flask, render_template, request
from redis import Redis

app = Flask(__name__)

app.config.from_prefixed_env("REDIS")
redis = Redis(host=app.config["HOST"], port=app.config["PORT"], decode_responses=True)


@app.route("/")
def index():
    ua = request.headers.get("User-Agent")
    ip = request.remote_addr

    visitor = f"{ua}_{ip}"

    redis.pfadd("visitors", visitor)

    unique_visitors = redis.pfcount("visitors")

    redis.incr("views")
    counter = str(redis.get("views"))

    return render_template(
        "index.html", counter=counter, unique_visitors=unique_visitors
    )
