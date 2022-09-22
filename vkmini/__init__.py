from .api import VkResponseException, set_loop

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.api import VkApi  # type: ignore
    class VkGroupApi(VkApi): ...
else:
    from .api import VkApi, VkGroupApi

from .exceptions import *
from .user_longpoll import LP
from .request import set_session, set_decoder
from .group_longpoll import GroupLP
from .keyboard import Keyboard, Button
