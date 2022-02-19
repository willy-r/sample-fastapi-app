from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_root():
    return {'message': 'Running'}


@app.get('/items/{item_id}')
async def get_item_by_id(item_id: int):
    return {
        'item': {
            'item_id': item_id,
            'name': f'item_{item_id}',
        }
    }
