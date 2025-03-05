from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = environ.get('USR_MNG_SECRET_KEY', None)
    PASSWORD_SALT = environ.get(
        'USR_MNG_PASSWORD_SALT', None)
