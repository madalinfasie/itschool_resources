import random

import redis
import flask

app = flask.Flask(__name__)
cache = redis.Redis(host='my-redis', port=6379)


def get_random():
    if cache.get('random'):
        return cache.get('random').decode()

    nr = random.randint(1, 1000)
    cache.set('random', nr, ex=30)
    return nr


@app.route('/')
def index():
    return flask.jsonify({'number': get_random()})
