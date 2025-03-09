class APIException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


class InvalidEmailError(APIException):
    def __init__(self):
        super().__init__(
            message="Email does not meet the requirements.",
            status_code=400
        )


class InvalidPasswordError(APIException):
    def __init__(self):
        super().__init__(
            message="Password does not meet the requirements.",
            status_code=400
        )


class InvalidNameError(APIException):
    def __init__(self):
        super().__init__(
            message="Name does not meet the requirements.",
            status_code=400
        )


class InvalidUsernameError(APIException):
    def __init__(self):
        super().__init__(
            message="Username does not meet the requirements.",
            status_code=400
        )
