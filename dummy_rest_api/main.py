import dataclasses

import flask
import redis

import db


app = flask.Flask(__name__)
redis_db = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/users')
def get_all_users() -> flask.Response:
    """ Endpoint for returning all the users in the database
    This endpoint supports filtering by name and number_of_pets
    via query params
    """
    supported_filters = ('name', 'number_of_pets')
    query_params = flask.request.args
    users_repo = db.UsersRepository(redis_db)
    users = users_repo.get_users()

    for param in query_params:
        if param not in supported_filters:
            continue

        users = [user for user in users if user[param].lower() == query_params[param].lower()]

    return flask.jsonify(users)


@app.route('/users/add')
def create_user() -> flask.Response:
    """ Create a new user and return a json with the newly created user"""
    request_body = flask.request.data
    users_repo = db.UsersRepository(redis_db)
    new_user = db.User(
        id=request_body['id'],
        name=request_body['name'],
        date_of_birth=request_body['date_of_birth'],
        number_of_pets=request_body.get('number_of_pets')
    )
    users_repo.add_user(new_user)

    return flask.jsonify(dataclasses.asdict(new_user))


@app.route('/users/<id>')
def get_user_by_id(id: int) -> flask.Response:
    """ Get a user by its id """
    users_repo = db.UsersRepository(redis_db)
    return flask.jsonify(users_repo.get_user_by_id(int(id)))
