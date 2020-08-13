class VkResponseException(Exception):
    def __init__(self, error: dict):
        self.error_code = error.get('error_code', None)
        self.error_msg = error.get('error_msg', None)
        self.request_params = error.get('request_params', None)

class NetworkError(Exception):
    code: int
    def __init__(self, code: int):
        self.code = code

class TooManyRequests(Exception):
    data: dict
    def __init__(self, data: dict):
        self.data = data

class TokenInvalid(Exception): # не, ну внатуре же
    pass