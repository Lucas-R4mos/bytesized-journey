from argon2 import PasswordHasher
from flask import Flask


hasher = PasswordHasher()


def encrypt(text: str, app: Flask):
    salt = bytes(app.config['PASSWORD_SALT'], "utf-8")
    return hasher.hash(text, salt=salt)
