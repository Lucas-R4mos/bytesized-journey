from utils import validators


class Users:
    id: int
    email: str
    password: str
    name: str
    username: str
    uniquifier_token: str
    active: bool
    role_id: int
    bio: str
    created_at: str
    updated_at: str

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def create(cls, email, name, username, password, role_id):
        raise NotImplementedError

    @classmethod
    def get_by_email(cls, email):
        raise NotImplementedError

    @classmethod
    def get_by_page(cls, page, **kwargs):
        raise NotImplementedError

    def update(self, name, username, bio):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def change_password(self, old_password, new_password):
        raise NotImplementedError

    @staticmethod
    def _validate_email(email):
        return validators.validate_email(email)

    @staticmethod
    def _validate_password(password):
        return validators.validate_password(password)

    @staticmethod
    def _validate_name(name):
        return validators.validate_name(name)

    @staticmethod
    def _validate_username(username):
        return validators.validate_username(username)
