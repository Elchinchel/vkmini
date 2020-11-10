from .api import VkResponseException, set_loop

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.api import VkApi
else:
    from .api import VkApi

from .exceptions import *
from .user_longpoll import LP
from .group_longpoll import LPGroup
from .keyboard import Keyboard, Button
