from fastapi import APIRouter, HTTPException

from utils.fake_db import FakeDB
from schemas.items import CreateItem, UpdateItem


router = APIRouter(prefix='/items', tags=['items'])
fdb_api = FakeDB()


@router.get('/')
async def get_all_items():
    return fdb_api.get_items()


@router.get('/{item_id}')
async def get_item_by_id(item_id: int):
    try:
        item = fdb_api.get_item(item_id)
        return item
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))


@router.post('/')
async def create_item(item: CreateItem):
    new_item = fdb_api.add_item(item.dict())
    return {
        'item_id': len(fdb_api.get_items()),
        'new_item': new_item,
    }


@router.patch('/{item_id}')
async def update_item_by_id(item_id: int, item: UpdateItem):
    try:
        updated_fields = fdb_api.update_item(item_id, item.dict())
        return {
            'item_id': item_id,
            'updated_fields': updated_fields,
        }
    except Exception as err:
       raise HTTPException(status_code=404, detail=str(err))


@router.delete('/{item_id}')
async def delete_item_by_id(item_id: int):
    try:
        fdb_api.delete_item(item_id)
        return {'item_id': item_id}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))
