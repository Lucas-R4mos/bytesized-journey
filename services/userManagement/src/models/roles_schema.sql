CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) UNIQUE NOT NULL,
    description VARCHAR(100)
);

CREATE INDEX IF NOT EXISTS idx_role_name ON roles(name);

INSERT INTO roles (name, description)
VALUES
    ('admin', 'Adminstrative role, can do everything.'),
    ('writer', 'Writer role, can write and read articles.'),
    ('reader', 'Reader role, can only read articles.')
ON CONFLICT (name) DO NOTHING;