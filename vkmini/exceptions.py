class VkResponseException(Exception):
    request_data: dict
    error_code: int
    error_msg: str
    error_data: dict

    def __new__(cls, error: dict, request_data: dict = {}):
        obj = Exception.__new__(_error_map.get(error['error_code'], cls))
        obj.__init__(error, request_data)
        return obj

    def __reduce_ex__(self, _):
        return self.__class__, (self.error_data, self.request_data)

    def __init__(self, error: dict, request_data: dict = {}):
        self.error_code = error['error_code']
        self.error_msg = error['error_msg']
        self.request_data = request_data
        self.error_data = error

    def __str__(self) -> str:
        info = f'Ошибка ВК #{self.error_code}: {self.error_msg}'
        if self.request_data:
            info += f'\nПараметры запроса: {self.request_data}'
        return info

    def get_short_str(self) -> str:
        return f'#{self.error_code}: {self.error_msg}'


class NetworkError(Exception):
    code: int

    def __init__(self, code: int):
        self.code = code


class RateLimit(VkResponseException):
    """Rate limit reached (29) error"""


class CaptchaNeeded(VkResponseException):
    """Captcha needed (14) error"""


class FloodControl(VkResponseException):
    """Flood control (9) error"""


class TooManyRequests(VkResponseException):
    """Too many requests (6) error"""


class TokenInvalid(VkResponseException):
    """Token is not valid (5) error"""


_error_map = {
    5: TokenInvalid,
    6: TooManyRequests,
    9: FloodControl,
    14: CaptchaNeeded,
    29: RateLimit
}
