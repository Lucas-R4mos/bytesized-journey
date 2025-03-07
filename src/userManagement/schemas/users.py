from psycopg_pool import ConnectionPool


def create_users_table(pool: ConnectionPool):
    with open('schemas/users_schema.sql') as file:
        schema = file.read()

    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(schema)
            connection.commit()
