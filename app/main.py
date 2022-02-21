import uvicorn
from fastapi import FastAPI

from routers import items


app = FastAPI()

app.include_router(items.router)


@app.get('/', tags=['root'])
async def get_root():
    return {'message': 'Running'}


if __name__ == '__main__':
    PORT = 8080
    uvicorn.run('main:app', port=PORT, host='0.0.0.0', reload=True)
