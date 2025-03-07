from flask import Flask
from psycopg_pool import ConnectionPool
from schemas.roles import create_roles_table
from schemas.users import create_users_table


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

    create_roles_table(pool)
    create_users_table(pool)

    return pool
