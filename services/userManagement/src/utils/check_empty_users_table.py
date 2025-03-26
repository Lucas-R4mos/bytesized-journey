from flask import Flask
from psycopg_pool import ConnectionPool


def check_empty_users_table(app: Flask) -> bool:
    pool: ConnectionPool = app.db

    with pool.connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        (count,) = cur.fetchone()

    return count == 0
