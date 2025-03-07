import atexit
from flask import Flask
from psycopg_pool import ConnectionPool


def create_pool(app: Flask):
    config = app.config
    pool = ConnectionPool(
        conninfo=f"""
            host=userManagementDatabase
            port=5432
            dbname=userManagement
            user={config['USR_MNG_DB_USER']}
            password={config['USR_MNG_DB_PASSWORD']}
        """,
        min_size=1,
        max_size=10,
        open=True
    )
    atexit.register(pool.close)

    return pool
