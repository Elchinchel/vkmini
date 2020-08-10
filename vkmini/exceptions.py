class VkApiResponseException(Exception):# да, спиздил))0)
    def __init__(self, *args, **kwargs):
        self.error_code = kwargs.get('error_code', None)
        self.error_msg = kwargs.get('error_msg', None)
        self.request_params = kwargs.get('request_params', None)
        self.args = args
        self.kwargs = kwargs

class NetworkError(Exception):
    code: int
    def __init__(self, code: int):
        self.code = code

class TooManyRequests(Exception):
    data: dict
    def __init__(self, data: dict):
        self.data = data

class TokenInvalid(Exception): # не, ну внатуре
    pass