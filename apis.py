from typing import List, Dict

from fastapi import FastAPI

from model import AppItemResponse
from service import (get_apps, insert_app, delete_app, update_app)

app = FastAPI()

@app.get('/')
async def index():
    return {"hello": "world"}
@app.get('/apps', response_model=List[AppItemResponse])
async def apps():
    return get_apps()
@app.post('/apps', response_model=Dict[str, str])
async def apps(url:str):
    return insert_app(url)
@app.delete('/apps', response_model=Dict[str, str])
async def apps(item_id:int):
    return delete_app(item_id)
@app.put('/apps', response_model=Dict[str, str])
async def apps(item_id:int, url:str):
    return update_app(item_id, url)