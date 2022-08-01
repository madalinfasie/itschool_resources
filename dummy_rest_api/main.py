import dataclasses
import os

import flask

import db


app = flask.Flask(__name__)
DB_PATH = f'{os.path.dirname(__file__)}/db.json'


@app.route('/users')
def get_all_users() -> flask.Response:
    """ Endpoint for returning all the users in the database
    This endpoint supports filtering by name and number_of_pets
    via query params
    """
    supported_filters = ('name', 'number_of_pets', 'date_of_birth')
    query_params = flask.request.args
    if not os.path.exists(DB_PATH):
        return flask.Response('No data in database', status=400)

    with open(DB_PATH, 'r') as f:
        users_repo = db.UsersRepository(f)
        users = users_repo.get_users()

    for param in query_params:
        if param not in supported_filters:
            continue

        users = [user for user in users if user[param].lower() == query_params[param].lower()]

    return flask.jsonify(users)


@app.route('/users/add', methods=['POST'])
def create_user() -> flask.Response:
    """ Create a new user and return a json with the newly created user"""
    request_body = flask.request.get_json()
    new_user = db.User(
            id=request_body['id'],
            name=request_body['name'],
            date_of_birth=request_body['date_of_birth'],
            number_of_pets=request_body.get('number_of_pets')
        )

    with open(DB_PATH, 'w+') as f:
        users_repo = db.UsersRepository(f)
        try:
            users_repo.add_user(new_user)
        except db.UserAlreadyExistsError as e:
            return flask.Response(str(e), status=400)

    return flask.jsonify(dataclasses.asdict(new_user))


@app.route('/users/<id>')
def get_user_by_id(id: int) -> flask.Response:
    """ Get a user by its id """
    with open(DB_PATH, 'r') as f:
        users_repo = db.UsersRepository(f)
        return flask.jsonify(users_repo.get_user_by_id(int(id)))
