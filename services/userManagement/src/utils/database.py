from flask import Flask
from models import create_tables
from psycopg_pool import ConnectionPool


def connect_to_db(app: Flask):
    config = app.config
    pool = ConnectionPool(
        conninfo=f"""
            host=userManagementDatabase
            port=5432
            dbname=userManagement
            user={config['USR_MNG_DB_USER']}
            password={config['USR_MNG_DB_PASSWORD']}
        """,
        max_size=20,
        open=True
    )

    create_tables(pool)

    return pool
