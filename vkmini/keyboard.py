import json
from enum import Enum
from typing import Any, Dict, List, Union, Literal


__all__ = (
    'Button',
    'FormattableButton',
    'Keyboard'
)


ButtonColors = Literal[
    'primary',  # Обычная
    'secondary',  # "Бледная"
    'positive',  # Зелёная
    'negative',  # Красная
]
ButtonTypes = Literal[
    'text',
    'vkpay',
    'location',
    'callback',
    'open_app',
    'open_link',
]


class Button:
    class Color(str, Enum):
        PRIMARY = 'primary'
        'Синяя, по умолчанию'
        SECONDARY = 'secondary'
        'Бледно-синяя'
        POSITIVE = 'positive'
        'Зеленая'
        NEGATIVE = 'negative'
        'Красная'

    class Type(str, Enum):
        TEXT = 'text'
        VKPAY = 'vkpay'
        LOCATION = 'location'
        CALLBACK = 'callback'
        OPEN_APP = 'open_app'
        OPEN_LINK = 'open_link'

    payload: Dict[str, Any]
    color: str
    label: str
    type: str

    def __init__(
            self,
            label: str,
            payload: dict,
            type: str = Type.TEXT,
            color: str = Color.PRIMARY
    ):
        self.payload = payload
        self.color = color
        self.label = label
        self.type = type

    def __str__(self) -> str:
        return self.as_kb().jsonize()

    def __format_button__(self, data: Dict[str, Any]) -> 'Button':
        return self

    def as_kb(self) -> 'Keyboard':
        """
        Returns:
            Keyboard: клавиатура с одной кнопкой
        """
        return Keyboard(self)

    def copy(self):
        cls = type(self)
        return cls(self.label, self.payload, self.type, self.color)

    @property
    def obj(self):
        return {
            'action': {
                'type': self.type,
                'label': self.label,
                'payload': json.dumps(self.payload, ensure_ascii=False)
            },
            'color': self.color
        }


# XXX
class FormattableButton(Button):
    """
    Позволяет не создавать клавиатуру каждый раз, когда нужно поменять
    пару параметров в `payload` кнопки.

    Для переопределения способа форматирования нужно создать дочерний от
    этого класс и переопределить метод `__format_button__`

    По умолчанию метод обновляет ключи,
    если они не представлены в payload, указанной при создании

    Использование:
    ```
    keyboard = Keyboard([
        Button('Обычная кнопка', {'hello': 'world'}),
        FormattableButton('Форматируемая кнопка', {'hello': 'world'})
    ])

    data = {
        'user_id': 8_800_555,
        'hello': 'bye',  # уже существующий ключ не будет перезаписан
        'type': 'xyz'
    }
    formatted_kb = keyboard.format(data)  # вернёт клавиатуру с форматированными кнопками

    formatted_kb.jsonize()
    >>> ... "payload": {"hello": "world", "user_id": 8800555, "type": "xyz"}
    ```
    """

    def __format_button__(self, data: Dict[str, Any]) -> 'Button':
        """
        Args:
            data -- словарь, переданный в Keyboard.format()

        Returns:
            Новый экземпляр Button, payload которого была отформатирована
        """
        payload = data.copy()
        payload.update(self.payload)
        return Button(self.label, payload, self.type, self.color)


class Keyboard:
    buttons: List[List[Button]]
    one_time: bool
    inline: bool

    def __init__(
            self,
            buttons: Union[Button, List[Button], List[List[Button]], None] = None,
            inline: bool = True,
            one_time: bool = False
    ):
        if not buttons:
            self.buttons = []
        elif isinstance(buttons, list) and \
                all(isinstance(bts, list) for bts in buttons):
            self.buttons = buttons  # type: ignore
        else:
            self.buttons = []
            self.add_buttons(buttons)  # type: ignore

        if inline and one_time:
            raise ValueError('inline и one_time -- взаимоисключающие параметры')
        self.inline = inline
        self.one_time = one_time

    def __str__(self) -> str:
        return self.jsonize()

    def add_new_button(self,
                       label: str,
                       payload: dict,
                       type: Button.Type = Button.Type.TEXT,
                       color: Button.Color = Button.Color.PRIMARY):
        self.add_buttons(Button(label, payload, type, color))

    def add_buttons(self, buttons: Union[Button, List[Button]]):
        if isinstance(buttons, Button):
            buttons = [buttons]
        self.buttons.append(buttons)

    def jsonize(self) -> str:
        return json.dumps({
            'one_time': self.one_time,
            'inline': self.inline,
            'buttons': [[btn.obj for btn in line] for line in self.buttons]
        }, ensure_ascii=False)

    def copy(self) -> 'Keyboard':
        return Keyboard([
            [btn.copy() for btn in line] for line in self.buttons
        ])

    def format(self, data: Dict[str, Any]) -> 'Keyboard':
        formatted_keyboard = Keyboard()
        for btn_line in self.buttons:
            formatted_keyboard.add_buttons(
                [btn.__format_button__(data) for btn in btn_line]
            )
        return formatted_keyboard

    format.__doc__ = FormattableButton.__doc__
