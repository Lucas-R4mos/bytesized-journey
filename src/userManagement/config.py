from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = environ.get('SECRET_KEY', None)
