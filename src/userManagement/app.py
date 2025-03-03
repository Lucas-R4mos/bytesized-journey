from os import environ
from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host=environ.get('USR_MNG_HOST'),
        port=environ.get('USR_MNG_PORT')
    )
