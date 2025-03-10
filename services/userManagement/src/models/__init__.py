from psycopg_pool import ConnectionPool


def create_tables(pool: ConnectionPool):
    table_names = ('roles', 'users')

    for table in table_names:
        with open(f'schemas/{table}_schema.sql') as file:
            schema = file.read()

        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(schema)
                connection.commit()
