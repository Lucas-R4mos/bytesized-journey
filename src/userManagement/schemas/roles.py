from psycopg_pool import ConnectionPool


def create_roles_table(pool: ConnectionPool):
    with open('schemas/roles_schema.sql') as file:
        schema = file.read()

    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(schema)
            connection.commit()
