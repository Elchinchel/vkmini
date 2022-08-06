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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.error_code})'

    def __str__(self) -> str:
        info = f'Ошибка ВК #{self.error_code}: {self.error_msg}'
        if self.request_data:
            info += f'\nПараметры запроса: {self.request_data}'
        return info

    def get_short_str(self) -> str:
        return f'#{self.error_code}: {self.error_msg}'


class NetworkError(Exception):
    """Ошибка сети при выполнении запроса"""
    code: int

    def __init__(self, code: int):
        self.code = code


class RateLimit(VkResponseException):
    """Достигнут лимит на вызов метода"""


class CaptchaNeeded(VkResponseException):
    """Необходимо решить капчу и повторить запрос"""


class FloodControl(VkResponseException):
    """Flood control, слишком много капч (пользователь) или сообщений (группа)"""


class TooManyRequests(VkResponseException):
    """Слишком много запросов"""


class TokenInvalid(VkResponseException):
    """Недействительный токен (5 для пользователей, 27 для групп)"""


_error_map = {
    5: TokenInvalid,
    27: TokenInvalid,
    6: TooManyRequests,
    9: FloodControl,
    14: CaptchaNeeded,
    29: RateLimit
}
