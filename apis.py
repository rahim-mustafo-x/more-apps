from fastapi import FastAPI
from service import (get_apps, insert_app, delete_app, update_app)

app = FastAPI()

@app.get('/')
async def index():
    return {"hello": "world"}
@app.get('/apps')
async def apps():
    return get_apps()
@app.post('/apps')
async def apps(url:str):
    return insert_app(url)
@app.delete('/apps')
async def apps(item_id:int):
    return delete_app(item_id)
@app.put('/apps')
async def apps(item_id:int, url:str):
    return update_app(item_id, url)