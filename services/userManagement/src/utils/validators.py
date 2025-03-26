import re
from utils.exceptions import (
    InvalidEmailError,
    InvalidNameError,
    InvalidPasswordError,
    InvalidUsernameError
)


UNICODE_LETTERS = r'a-zA-ZÀ-ÖØ-öø-ÿ'              # Latin
UNICODE_LETTERS += r'\u4E00-\u9FFF'               # Chinese
UNICODE_LETTERS += r'\u3040-\u309F\u30A0-\u30FF'  # Japanese
UNICODE_LETTERS += r'\u0400-\u04FF'               # Cyrillic
UNICODE_LETTERS += r'\u0370-\u03FF'               # Greek
UNICODE_LETTERS += r'\u0600-\u06FF'               # Arabic
UNICODE_LETTERS += r'\u00B7\u02BF'                # · and ʿ


def validate_email(email: str) -> str:
    """
        Email validator according to RFC 5322
        https://datatracker.ietf.org/doc/html/rfc5322#section-3.4.1
    """
    if len(email) > 254:
        raise InvalidEmailError()

    parts = email.split('@')
    if len(parts) != 2:
        raise InvalidEmailError()

    local_part, domain = parts

    if (
        len(local_part) > 64 or
        not re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+$", local_part) or
        local_part.startswith('.') or
        local_part.endswith('.') or
        '..' in local_part or
        '.' not in domain
    ):
        raise InvalidEmailError()

    labels = domain.split('.')
    for label in labels:
        if (
            len(label) > 63 or
            len(label) < 1 or
            not re.match(r"^[a-zA-Z0-9-]+$", label) or
            label.startswith('-') or
            label.endswith('-')
        ):
            raise InvalidEmailError()

    return email


def validate_name(name: str) -> str:
    """
        Names must:
            1. Have at least 2 characters
            2. Not have more than 60 characters
        Names can contain characters from the following alphabets:
            1. Latin
            2. Chinese
            3. Japanese
            4. Cyrillic
            5. Greek
            6. Arabic
    """
    pattern = re.compile(
        r'^[' + UNICODE_LETTERS + r'\s\'.-]+$',
        re.UNICODE
    )

    normalized_name = ' '.join(name.strip().split())

    if (
        len(normalized_name) > 60 or
        len(normalized_name) < 2 or
        not pattern.fullmatch(normalized_name)
    ):
        raise InvalidNameError()

    return normalized_name


def validate_password(password: str) -> str:
    """
        Passwords must:
            1. Have at least 8 characters
            2. Not have more than 100 characters
            3. Have at least 1 number
            4. Have at least 1 uppercase letter
            5. Have at least 1 lowercase letter
            6. Have at least 1 special character
            7. Not have more than 3 consecutive characters
    """
    if (
        len(password) < 8 or
        len(password) > 100 or
        not re.search(r"[0-9]", password) or
        not re.search(r"[A-Z]", password) or
        not re.search(r"[a-z]", password) or
        not re.search(r"[^a-zA-Z0-9]", password) or
        re.search(r"(.)\1{2}", password)
    ):
        raise InvalidPasswordError()

    return password


def validate_username(username: str) -> str:
    """
        Usernames must:
            1. Have at least 3 characters
            2. Not have more than 20 characters
            3. Not start or end with a special character
            4. Have only a-z, 0-9, _, ., -
            5. Not have more than 3 consecutive characters
    """
    username = username.strip().lower()

    if (
        len(username) < 3 or
        len(username) > 20 or
        not re.match(r'^[a-z0-9][a-z0-9_.-]{1,18}[a-z0-9]$', username) or
        re.search(r'(.)\1{2}', username)
    ):
        raise InvalidUsernameError()

    return username
