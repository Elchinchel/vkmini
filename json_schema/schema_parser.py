# сама схема тут > https://github.com/VKCOM/vk-api-schema

import re
import json
from copy import deepcopy
from typing import Dict, List, NoReturn
from os.path import join, dirname
from itertools import chain
from collections import defaultdict


def open_schema(name: str, key: str):
    with open(join(dirname(__file__), f'{name}.json'), 'r', encoding='utf-8') as file:
        return json.loads(file.read())[key]


types = {
    'boolean': 'Flag',
    'integer': 'int',
    'number': 'float',
    'string': 'str',
    '__none__': 'None',
}


RESTRICTED_NAMES = {'from', 'class', 'global'}


objects_to_type_ignore = set([
    'newsfeed_item_wallpost',  # дубликаты полей в суперклассах.
        # (это можно решить, если не сразу в строки объекты упихивать, а
        #  сделать промежуточное представление, тогда можно
        #  собрать новый класс из полей суперкласса)
])


def check_restricted(name: 'str | None') -> bool:
    if name is None:
        return False
    if name in RESTRICTED_NAMES:
        return True
    if name[0].isdigit():
        return True
    return False


def get_type(type) -> str:
    if isinstance(type, list):
        if len(type) > 1:
            return f"Union[{', '.join(get_type(t) for t in type)}]"
        type = type[0]

    if type in types:
        return types[type]

    raise_unknown(type)


class Item:
    name: str
    raw_value: str

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Item):
            return False
        for k, v in vars(value).items():
            if getattr(self, k, None) != v:
                return False
        return True

    @property
    def body(self) -> str:
        return self.raw_value

    @property
    def value(self) -> str:
        return f'{self.name}: {self.raw_value}'

    @property
    def as_alias(self) -> str:
        return f'{self.name}: TypeAlias = {self.raw_value}'

    def __init__(self, name, raw_value) -> None:
        self.name = name
        self.raw_value = raw_value

    def optionalize(self):
        if 'Optional' not in self.raw_value:
            self.raw_value = f'Optional[{self.raw_value}]'


class Enum(Item):
    raw_literal: str

    @property
    def literal(self) -> str:
        return f'{self.raw_value} = {self.raw_literal}'

    @property
    def as_alias(self) -> str:
        return f'{self.raw_value}: TypeAlias = {self.raw_literal}'

    @property
    def body(self) -> str:
        return self.raw_literal


class Object(Item):
    lines: List[str]

    @property
    def body(self) -> str:
        print(f'объект {self.name} пропущен')
        return 'Dict[str, Any]'

    @property
    def value(self) -> str:
        raise TypeError('это нужно использовать не так')

    raw_value = value  # type: ignore

    def __init__(self, name) -> None:
        self.name = name
        self.lines = []


def indent(depth) -> str:
    return '    ' * depth


def raise_unknown(item) -> NoReturn:
    print(json.dumps(item, ensure_ascii=False, indent=4))
    raise ValueError('я такого не знаю')


def escape(item, type):
    if type == 'string':
        return '\'' + str(item) + '\''
    if type == 'integer':
        return str(item)
    raise ValueError('а как какать')


def parse_ref(ref: str, escape=True) -> str:
    namespace, _, name = ref.split('/')
    namespace = namespace.partition('.')[0]

    if namespace == '#' or context_name == namespace:
        result = name
    else:
        result = f'{namespace}.{name}'

    return ('\'' + result + '\'') if escape else result


def parse_item(name: 'str | None', item: dict, *, enum_as_type=False):
    if '$ref' in item:
        return Item(name, parse_ref(item['$ref']))

    type = item['type']

    if (enum := item.get('enum')):
        if enum_as_type and (names := item.get('enumNames')):
            obj = Object(name)
            obj.lines.append(f"{name} = Literal[")
            for i, value in enumerate(enum):
                obj.lines.append(indent(1) + escape(value, type))
                if i < len(enum) -1:
                    obj.lines[-1] += ','
                obj.lines[-1] += f'  # {names[i]}'
            obj.lines.append(']')
            return obj
        else:
            return Item(name,
                f"Literal[{', '.join(escape(i, type) for i in enum)}]"
            )

    if isinstance(type, list) or type in types:
        return Item(name, get_type(type))

    if type == 'array':
        if 'items' not in item:
            return Item(name, 'List[Any]')

        items = item['items']

        if '$ref' in items:
            return Item(name, f"List[{parse_ref(items['$ref'])}]")

        if 'allOf' in items:
            return Item(name,
                f"Union[{', '.join(parse_item('', i).body for i in items['allOf'])}]"
            )

        type = items['type']

        if type == 'array':
            arr_item = parse_item(name, items['items'])

            if isinstance(arr_item, Object):
                raise_unknown(items['items'])

            if isinstance(arr_item, Enum):
                return Item(name, arr_item.raw_literal)

            return Item(name, arr_item.raw_value)

        if type == 'object':
            print(f'объект {name} пропущен')
            return Item(name, 'Dict[str, Any]')

        if isinstance(type, list):
            for t in type:
                if t not in types:
                    raise_unknown(item)
        elif type not in types:
            raise_unknown(item)

        if 'enum' not in items:
            return Item(name, f'List[{get_type(type)}]')

        enum = Enum(name, f'{name}_enum')
        enum.raw_literal = (
            f"Literal[{', '.join(escape(i, type) for i in items['enum'])}]"
        )
        return enum

    if type == 'object':
        if 'oneOf' in item:
            return Item(name,
                f"Union[{', '.join(parse_item('', i).body for i in item['oneOf'])}]"
            )

        allOf = item.get('allOf')
        properties = item.get('properties')

        if not (properties or allOf):
            print(f'не вкурил объект {name}')
            return Item(name, 'Dict[str, Any]')

        obj = Object(name)

        parents = []

        if allOf:
            for i in allOf:
                if '$ref' in i:
                    parents.append(parse_ref(i['$ref'], escape=False))
                if 'properties' in i:
                    if not properties:
                        properties = i['properties']
                    else:
                        raise_unknown(allOf)

        if not parents:
            parents.append('TypedDict')

        obj.lines.append(f"class {name}({', '.join(parents)}):")

        assert isinstance(item.get('required', False), bool)

        if properties:
            for name, property in properties.items():
                prop = parse_item(name, property)
                if isinstance(prop, Enum):
                    object_enums[prop.raw_value] = prop  # noqa

                if property.get('required'):
                    prop_info = f'{name}: {prop.raw_value}'
                else:
                    prop_info = f'{name}: NotRequired[{prop.raw_value}]'

                if check_restricted(name):
                    prop_info = '# ' + prop_info

                if (desc := property.get('description')):
                    prop_info += '  # ' + desc

                obj.lines.append(indent(1) + prop_info)
        else:
            obj.lines[-1]+= ' ...'

        if (desc := item.get('description')):
            obj.lines.insert(1, f"{indent(1)}'''{desc}'''")

        return obj

    raise_unknown(item)


def parse_method(method: dict, overload: 'str | None' = None):
    if '.' not in method['name']:
        print(f'Skipped {method["name"]!r}')
        return
    group = method['name'].split('.')[0]
    name = method['name'].split('.')[1]

    if group not in method_groups:
        method_groups[group] = []

    params = ['self']
    overloads = []
    method_info = []
    params_with_defaults = []

    parameters = sorted(
        method.get('parameters', []),
        key=lambda param: bool(param.get('required')),
        reverse=True
    )

    def set_param_value(repl_method, param_name, field, value):
        for param in repl_method['parameters']:
            if param['name'] == param_name:
                param[field] = value

    if (fields_response := method['responses'].get('fieldsResponse')):
        overload_method = deepcopy(method)
        overload_method['responses'] = {'response': fields_response}
        set_param_value(overload_method, 'fields', 'required', True)
        overloads.append(parse_method(overload_method, 'fields'))
        set_param_value(method, 'fields', 'type', '__none__')

    def wrap_List(param: str) -> str:
        if re.match(r'Union\[.*str.*\]', param):
            return param
        if param == 'List[str]':
            return 'str'
        if (listed_match := re.match(r'List\[(.+)\]', param)) is not None:
            if re.match(r'Union\[.*str.*\]', listed_match[1]):
                return listed_match[1]
            return f'Union[{listed_match[1]}, str]'
        return param

    for param in parameters:
        if param['name'] in {'global'}:
            continue

        param_name = param['name']
        param_parsed = parse_item(param_name, param)

        if isinstance(param_parsed, Enum):
            param_parsed.raw_value = f'{group}_{param_parsed.name}_enum'
            existing = method_enums.get(param_parsed.raw_value)
            if existing and param_parsed != existing:
                raise Exception('два разных енума с одним именем')
            method_enums[param_parsed.raw_value] = param_parsed

        if 'default' in param:
            default = param['default']
            if isinstance(default, str):
                if default.isdigit():
                    default = int(default)
                else:
                    default = f"\'{default}\'"
            if default is None:
                param_parsed.optionalize()
            if isinstance(default, list) and all(map(lambda x: isinstance(x, str), default)):
                default = f"\'{','.join(default)}\'"
            param_parsed.raw_value = wrap_List(param_parsed.raw_value)
            params_with_defaults.append(f"{param_parsed.value} = {default}")
        else:
            value = wrap_List(param_parsed.raw_value)
            if param.get('required'):
                params.append(f'{param_parsed.name}: {value}')
            else:
                params.append(
                    f'{param_parsed.name}: Optional[{value}] = None'
                )

    # if len(method['responses']) > 1:
    #     print(f'NOTE: {method["name"]} has few responses: {method["responses"]}')

    # resp_obj = method['responses'].get('response')
    # if not resp_obj:
    #     resp_obj = method['responses'].get('baseResponse')
    # if not resp_obj:
    #     resp_obj = method['responses'].get('deprecatedResponse')
    # if not resp_obj:
    #     raise_unknown(method['responses'])

    return_values = []
    for resp_obj in method['responses'].values():
        ret_val = parse_item(None, resp_obj)
        if isinstance(ret_val, Enum):
            return_values.append(ret_val.raw_literal)
        else:
            return_values.append(ret_val.raw_value)

    if len(return_values) == 1:
        joined_return = return_values[0]
    else:
        joined_return = f'Union[{", ".join(return_values)}]'

    params.extend(params_with_defaults)

    if len(params) > 1:
        params.insert(1, '*')

    method_info.append(
        f"async def {name}({', '.join(params)}, **kwargs: Any) -> {joined_return}:"
    )
    if overload is not None:
        return f'{method_info[0]} ...'

    if 'description' in method:
        method_info.append(f"{indent(1)}'''{method['description']}'''")
    else:
        method_info[-1] += ' ...'

    if overloads:
        method_info.insert(0, '@overload')
        for overload_info in reversed(overloads):
            method_info.insert(0, overload_info)
            method_info.insert(0, '@overload')

    update_imports('methods', method_info)
    method_groups[group].append(method_info)


def parse_response(name: str, response: dict):
    lines = []

    if response['type'] == 'object':
        if len(response['properties']) > 1:
            raise_unknown(response)
        response = response['properties']['response']

    item = parse_item(name, response)

    if isinstance(item, Enum):
        lines.append(item.literal)

    if isinstance(item, Object):
        lines = item.lines
    else:
        lines.append(item.as_alias)
        if (desc := response.get('description')):
            lines[-1] += f"  # {desc}"

    update_imports('responses', lines)
    api_responses.append(lines)


def parse_object(name: str, object: dict):
    lines = []

    item = parse_item(name, object, enum_as_type=True)

    if isinstance(item, Enum):
        lines.append(item.literal)

    if isinstance(item, Object):
        lines = item.lines
        if name in objects_to_type_ignore:
            lines[0] += '  # type: ignore'
    else:
        lines.append(item.as_alias)
        if (desc := object.get('description')):
            lines[-1] += f"  # {desc}"

    update_imports('objects', lines)
    api_objects.append(lines)


def clean_import_name(inm):
    return re.search(r"\w+", inm)[0]  # noqa  # pyright: ignore[reportOptionalSubscript]

imports = defaultdict(set)
known_import_names = {
    'typing': ['TYPE_CHECKING', 'Any', 'Dict[', 'List[', 'Union[', 'Literal[', 'Optional[', '@overload', 'Protocol'],
    'typing_extensions': ['TypedDict', 'TypeAlias', 'NotRequired'],
    'vkmini.types': ['objects.', 'methods.', 'responses.'],
}
import_names_modules = {}
for modname, impnames in known_import_names.items():
    for iname in impnames:
        import_names_modules[clean_import_name(iname)] = modname

import_regex = re.compile(
    '(%s)' % '|'.join(
        re.escape(v) for v in chain(*known_import_names.values())
    )
)

def update_imports(result_name: str, lines):
    for line in lines:
        for match in import_regex.finditer(line):
            imports[result_name].add(match[0])

def gen_imports(result_name: str, additional: 'list[str]') -> 'list[str]':
    modules_imports = defaultdict(list)
    for iname in imports[result_name].union(set(additional)):
        iname = clean_import_name(iname)
        modules_imports[import_names_modules[iname]].append(iname)

    return [
        f'from {k} import {", ".join(sorted(v))}'
            for k, v in modules_imports.items()
    ]


def open_result_file(filename: str, mode: str):
    return open(
        join(dirname(__file__), 'result', filename),
        mode,
        encoding='utf-8'
    )


context_name = 'methods'
method_enums: Dict[str, Enum] = {}
method_groups: Dict[str, List[List[str]]] = {}
for method in open_schema('methods', 'methods'):
    try:
        parse_method(method)
    except Exception:
        print(json.dumps(method, ensure_ascii=False, indent=4))
        raise


def add(indent_depth: int, code: str):
    print(indent(indent_depth) + code, file=file)


with open_result_file('methods.pyi', 'w') as file:
    for line in gen_imports('methods', ['TypeAlias', 'Protocol']):
        add(0, line)
    add(0, '')
    add(0, '')
    add(0, 'class _VkMethod(Protocol):')
    add(1, 'async def __call__(self, **kwargs) -> Any: ...')
    add(0, '')
    add(0, 'Flag: TypeAlias = int')
    add(0, '')

    for enum in method_enums.values():
        add(0, enum.as_alias)

    add(0, '')
    add(0, '')

    for group in method_groups:
        add(0, f'class {group}:')
        add(1,  'def __getattr__(self, __name: str) -> _VkMethod: ...')
        add(0,  '')
        for method in method_groups[group]:
            for line in method:
                add(1, line)
            add(0, '')

with open_result_file('method_groups.pyi', 'w') as file:
    add(0, 'from vkmini.types import methods')
    add(0, '')
    for group in method_groups:
        add(0, f'{group}: methods.{group}')

    add(0, '')
    add(0, '_API_METHOD_GROUPS = (')
    for group in method_groups:
        add(1, f'\'{group}\',')
    add(0, ')')


context_name = 'responses'
api_responses: List[List[str]] = []
for name, response in open_schema('responses', 'definitions').items():
    parse_response(name, response)


with open_result_file('responses.py', 'w') as file:
    for line in gen_imports('responses', []):
        add(0, line)
    add(0, '')
    add(0, '')
    add(0, 'Flag: TypeAlias = int')
    add(0, '')

    for response in api_responses:
        for line in response:
            add(0, line)
        add(0, '')


context_name = 'objects'
api_objects: List[List[str]] = []
object_enums = {}
for name, object in open_schema('objects', 'definitions').items():
    parse_object(name, object)


with open_result_file('objects.py', 'w') as file:
    for line in gen_imports('objects', []):
        add(0, line)
    add(0, '')
    add(0, '')
    add(0, 'Flag: TypeAlias = int')
    add(0, '')

    for enum in object_enums.values():
        add(0, enum.as_alias)

    add(0, '')
    add(0, '')

    variables = []
    remaining_objects = []
    for obj in api_objects:
        if (match := re.match(r'class (\w+)\((.+?)\)', obj[0])):
            if match[2] == 'TypedDict':
                bases = []
            else:
                bases = [n.strip() for n in match[2].split(',')]
            remaining_objects.append({'obj': obj, 'name': match[1], 'bases': bases})
        else:
            variables.append(obj)

    remaining_objects.sort(key=lambda x: len(x['bases']))
    remaining_objects.reverse()

    api_objects_sorted = []
    existing_names = set()
    deferred_objects = []
    while remaining_objects or deferred_objects:
        if deferred_objects:
            added_objs = []
            for obj in deferred_objects:
                if all(map(lambda b: b in existing_names, obj['bases'])):
                    existing_names.add(obj['name'])
                    added_objs.append(obj)
                    api_objects_sorted.append(obj)
            for obj in added_objs:
                deferred_objects.remove(obj)
            if not remaining_objects and not added_objs:
                print(json.dumps(list(remaining_objects), indent=4, ensure_ascii=False))
                print(json.dumps(list(deferred_objects), indent=4, ensure_ascii=False))
                raise Exception('циклические ссылки')

        if remaining_objects:
            obj = remaining_objects.pop()
            if all(map(lambda b: b in existing_names, obj['bases'])):
                existing_names.add(obj['name'])
                api_objects_sorted.append(obj)
            else:
                deferred_objects.append(obj)


    for obj in variables:
        for line in obj:
            add(0, line)
        add(0, '')
    for obj in api_objects_sorted:
        for line in obj['obj']:
            add(0, line)
        add(0, '')

del object_enums


with open_result_file('exceptions.py', 'w') as file:
    add(0,
'''class VkResponseException(Exception):
    """
    Описывает ошибку VK API

    `request_data` -- параметры запроса
    `error_code` -- код ошибки
    `error_msg` -- сообщение ошибки
    `error_data` -- объект из поля 'error' ответа VK API, описывающий ошибку
    """
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
            info += f'\\nПараметры запроса: {self.request_data}'
        return info

    def get_short_str(self) -> str:
        return f'#{self.error_code}: {self.error_msg}'


class NetworkError(Exception):
    """Ошибка сети при выполнении запроса"""
    code: int

    def __init__(self, code: int):
        self.code = code


class TokenInvalid(VkResponseException):
    """
    Общая ошибка недействительного токена для групп, пользователей
    и приложений (коды 5, 27, 28)
    """
    ''')


    def prep_name(name: str) -> str:
        parts = name.split('_')
        return 'Vk' + ''.join(p.capitalize() for p in parts[1:])

    errors = []

    for name, error in open_schema('errors', 'errors').items():
        add(0, '')

        code = error['code']
        p_name = prep_name(name)
        errors.append((code, p_name))

        if p_name in {'VkErrorAuth', 'VkErrorGroupAuth', 'VkErrorAppAuth'}:
            base = 'TokenInvalid'
        else:
            base = 'VkResponseException'

        msg = f'class {p_name}({base}):'

        if 'global' in error:
            msg += '  # общая ошибка'

        add(0, msg)

        desc = f'(код {code})'

        if 'description' in error:
            desc += ' ' + error['description']

        add(1, f"'''{desc}'''")

    add(0, '')
    add(0, '')

    add(0, '_error_map = {')
    errors.sort(key=lambda x: x[0])
    for code, name in errors:
        add(1, f'{code}: {name},')
    add(0, '}')
