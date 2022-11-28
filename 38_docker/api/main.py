import requests

import flask


app = flask.Flask(__name__)


def _get_number():
    response = requests.get('http://random-generator:5001/')
    response.raise_for_status()
    return response.json()['number']


@app.route('/')
def index():
    try:
        return flask.Response(f'<h1>Your lucky number today is: {_get_number()}</h1>')
    except requests.exceptions.RequestException as e:
        print('Eroarea este: ', repr(e))
        return flask.Response('Unexpected error, sorry')

if __name__ == '__main__':
    app.run()