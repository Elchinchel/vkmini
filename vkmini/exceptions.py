class VkResponseException(Exception):
    request_data: dict
    error_code: int
    error_msg: str

    def __init__(self, error: dict, request_data: dict):
        self.error_code = error['error_code']
        self.error_msg = error['error_msg']
        self.request_data = request_data
        self.request_params = error.get('request_params', None)


class NetworkError(Exception):
    code: int

    def __init__(self, code: int):
        self.code = code


class TooManyRequests(VkResponseException):
    """Too many requests (6) error"""


class TokenInvalid(VkResponseException):
    """Token is not valid (5) error"""
