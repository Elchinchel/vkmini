import json

from enum import Enum
from typing import Any, List, Dict, Union, Literal


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
        PRIMARY = 'primary'      # Синяя, обычная
        SECONDARY = 'secondary'  # "Бледная"
        POSITIVE = 'positive'    # Зелёная
        NEGATIVE = 'negative'    # Красная

    class Type(str, Enum):
        TEXT = 'text'
        VKPAY = 'vkpay'
        LOCATION = 'location'
        CALLBACK = 'callback'
        OPEN_APP = 'open_app'
        OPEN_LINK = 'open_link'

    payload: str
    color: str
    label: str
    type: str

    def __init__(
            self,
            label: str,
            payload: Union[str, dict],
            type: Type = Type.TEXT,
            color: Color = Color.PRIMARY
    ):
        self.payload = payload
        if isinstance(self.payload, dict):
            self.payload = json.dumps(self.payload, ensure_ascii=False)
        self.color = color
        self.label = label
        self.type = type

    def __str__(self) -> str:
        return Keyboard(self).jsonize()

    def __format_button__(self, data: Dict[str, Any]) -> 'Button':
        return self

    def copy(self) -> 'Button':
        return Button(self.label, self.payload, self.type, self.color)

    @property
    def obj(self):
        return {
            'action': {
                'type': self.type,
                'label': self.label,
                'payload': self.payload
            },
            'color': self.color
        }


class FormattableButton(Button):
    """
    Позволяет не создавать клавиатуру каждый раз, когда нужно поменять
    пару параметров в `payload` или `label` кнопки.

    Форматирование осуществляется вызовом метода `.format` у объектов
    `payload` и `label`, для переопределения способа форматирования
    можно переопределить метод `__format_button__` у этого класса или
    при создании кнопки передавать вместо `str` экземпляры своего класса

    Использование:
    ```
    keyboard = Keyboard([
        Button('Обычная кнопка', 'статичная нагрузочка'),
        FormattableButton('Label с {label_var}', 'Payload с {payload_var}')
    ])

    data = {
        'label_var': 'ярлычком',
        'payload_var': 'нагрузочкой'
    }
    formatted_kb = keyboard.format(data)  # вернёт клавиатуру с форматированными кнопками

    formatted_kb.jsonize()
    >>> ... {"label": "Label с ярлычком", "payload": "Payload с нагрузочкой"}
    ```
    """
    def __format_button__(self, data: Dict[str, Any]) -> 'Button':
        return Button(self.label.format(**data),
                      self.payload.format(**data),
                      self.type,
                      self.color)


class Keyboard:
    buttons: List[List[Button]]
    one_time: bool
    inline: bool

    def __init__(
            self,
            buttons: Union[Button, List[Button], List[List[Button]]] = None,
            inline: bool = True,
            one_time: bool = False
    ):
        self.buttons = []
        if buttons is not None:
            self.add_buttons(buttons)
        if inline and one_time:
            raise ValueError('inline и one_time -- взаимоисключающие параметры')
        self.inline = inline
        self.one_time = one_time

    def __str__(self) -> str:
        return self.jsonize()

    def add_new_button(self,
                       label: str,
                       payload: Union[str, dict],
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
        return [[btn.copy() for btn in line] for line in self.buttons]

    def format(self, data: Dict[str, Any]) -> 'Keyboard':
        formatted_keyboard = Keyboard()
        for btn_line in self.buttons:
            formatted_keyboard.add_buttons(
                [btn.__format_button__(data) for btn in btn_line]
            )
        return formatted_keyboard

    format.__doc__ = FormattableButton.__doc__
