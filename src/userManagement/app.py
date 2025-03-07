from flask import Flask
from config import Config
from database import create_pool


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.db = create_pool(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000
    )
