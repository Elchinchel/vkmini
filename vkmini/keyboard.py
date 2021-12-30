from typing import List, Union
import json


class Button:
    payload: str
    color: str
    label: str
    type: str

    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    NEGATIVE = 'negative'
    POSITIVE = 'positive'

    def __init__(self,
                 label: str,
                 payload: Union[str, dict],
                 type: str = 'text',
                 color: str = 'primary') -> None:
        self.payload = payload
        if isinstance(self.payload, dict):
            self.payload = json.dumps(self.payload, ensure_ascii=False)
        self.color = color
        self.label = label
        self.type = type

    @property
    def obj(self):
        return {
            "action": {
                "type": self.type,
                "label": self.label,
                "payload": self.payload
            },
            "color": self.color
        }


class Keyboard:
    buttons: List[List[Button]] = []
    one_time: bool
    inline: bool

    def __init__(self,
                 buttons: Union[Button, List[Button]] = None,
                 inline: bool = True,
                 one_time: bool = False) -> None:
        if buttons is not None:
            self.add_buttons(buttons)
        if inline and one_time:
            raise ValueError(
                'inline и one_time -- взаимоисключающие параметры'
            )
        self.inline = inline
        self.one_time = one_time

    def add_buttons(self, buttons: Union[Button, List[Button]]):
        if isinstance(buttons, Button):
            buttons = [buttons]
        self.buttons.append(buttons)

    def jsonize(self, alt_buttons: List[List[Button]] = None) -> str:
        if alt_buttons is None:
            alt_buttons = self.buttons
        return json.dumps({
            "one_time": self.one_time,
            "inline": self.inline,
            "buttons": [[b.obj for b in li] for li in alt_buttons]
        }, ensure_ascii=False)

    # XXX: remove
    def format_and_jsonize(self, data: Union[tuple, dict]) -> str:
        buttons = []
        for line in self.buttons:
            button_line = []
            for button in line:
                button_line.append(Button(
                    button.label,
                    button.payload % data,
                    button.type,
                    button.color
                ))
            buttons.append(button_line)
        return self.jsonize(buttons)
    
    def format_label(self, data: Union[tuple, dict]) -> 'Keyboard':
        for line in self.buttons:
            for button in line:
                button.label = button.label % data
        return self

    def format_payload(self, data: Union[tuple, dict]) -> 'Keyboard':
        for line in self.buttons:
            for button in line:
                button.payload = button.payload % data
        return self
