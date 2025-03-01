from fastapi import FastAPI, status
from starlette.responses import JSONResponse

app = FastAPI()

@app.get('/ping/', status_code=status.HTTP_200_OK)
async def ping():
    return {'message': 'pong'}