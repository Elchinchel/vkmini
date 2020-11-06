from .api import VkApi, VkResponseException
from .exceptions import *
from .user_longpoll import LP
from .group_longpoll import LPGroup
from .keyboard import Keyboard, Button
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .methods.methods import messages
    VkApi.messages = messages
