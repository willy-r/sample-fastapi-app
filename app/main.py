import uvicorn
from fastapi import FastAPI

from fake_db import FakeDB
from schemas import CreateItem, UpdateItem

app = FastAPI()
fdb_api = FakeDB()


@app.get('/')
async def get_root():
    return {'message': 'Running'}


@app.get('/items')
async def get_all_items():
    return fdb_api.get_items()


@app.get('/items/{item_id}')
async def get_item_by_id(item_id: int):
    try:
        item = fdb_api.get_item(item_id)
        return item
    except Exception as err:
        return {'message': str(err)}


@app.post('/items')
async def create_item(item: CreateItem):
    new_item = fdb_api.add_item(item.dict())
    return {
        'item_id': len(fdb_api.get_items()),
        'new_item': new_item,
    }


@app.patch('/items/{item_id}')
async def update_item_by_id(item_id: int, item: UpdateItem):
    try:
        updated_fields = fdb_api.update_item(item.dict())
        return {
            'item_id': item_id,
            'updated_fields': updated_fields,
        }
    except Exception as err:
        return {'message': str(err)}


@app.delete('/items/{item_id}')
async def delete_item_by_id(item_id: int):
    try:
        fdb_api.delete_item(item_id)
        return {'item_id': item_id}
    except Exception as err:
        return {'message': str(err)}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
