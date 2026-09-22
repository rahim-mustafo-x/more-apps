from bs4 import BeautifulSoup
from requests import get
from config import parts
from database import Database
from camel_converter import to_camel
from dataclasses import is_dataclass, asdict
from collections.abc import Iterable, Mapping

database = Database()

def insert_app(url:str):
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = {}
    for tag, kwargs in parts.items():
        element = soup.find(tag, **kwargs)
        if not element:
            continue
        if tag == 'meta':
            value = element.get('content')
        elif tag == 'img':
            value = element.get('src')
        else:
            value = element.get_text(strip=True)
        data[tag] = value
    database.insert_app(
        name=data['span'],
        icon_url=data['img'],
        direct_url=url,
        description=data['meta']
    )
    return data
def update_app(item_id:int, url:str):
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = {}
    for tag, kwargs in parts.items():
        element = soup.find(tag, **kwargs)
        if not element:
            continue
        if tag == 'meta':
            value = element.get('content')
        elif tag == 'img':
            value = element.get('src')
        else:
            value = element.get_text(strip=True)
        data[tag] = value
    database.update_app(
        item_id=item_id,
        name=data['span'],
        icon_url=data['img'],
        direct_url=url,
        description=data['meta']
    )
    return data
def delete_app(item_id:int):
    database.delete_app(item_id)
def get_apps():
    return camelize_keys(database.get_apps())
def camelize_keys(obj):
    if isinstance(obj, Mapping):
        return {to_camel(k): camelize_keys(v) for k, v in obj.items()}
    elif is_dataclass(obj) and not isinstance(obj, type):
        return camelize_keys(asdict(obj))
    elif hasattr(obj, "model_dump"):  # Pydantic v2 model
        return camelize_keys(obj.model_dump())
    elif hasattr(obj, "dict"):  # Pydantic v1 model
        return camelize_keys(obj.dict())
    elif isinstance(obj, (list, tuple)) or (isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))):
        return [camelize_keys(item) for item in obj]
    else:
        return obj