from flask import Flask
from config import Config
from utils import (
    connect_to_db,
    check_empty_users_table
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.db = connect_to_db(app)

    @app.teardown_appcontext
    def close_app(exception):
        app.db.close()

    app.status = dict(
        allow_unauthenticated_registration=False
    )

    if check_empty_users_table(app):
        app.status['allow_unauthenticated_registration'] = True

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000
    )
