from bs4 import BeautifulSoup
from requests import get
from config import parts
from database import Database

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
    return database.insert_app(
        name=data['span'],
        icon_url=data['img'],
        direct_url=url,
        description=data['meta']
    )
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
    return database.update_app(
        item_id=item_id,
        name=data['span'],
        icon_url=data['img'],
        direct_url=url,
        description=data['meta']
    )
def delete_app(item_id:int):
    return database.delete_app(item_id)
def get_apps():
    try:
        return database.get_apps()
    except ResponseValidationError:
        return []