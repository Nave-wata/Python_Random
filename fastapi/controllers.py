from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def read_items(request: Request, token: str = Depends(oauth2_scheme)):
    return {"token": token}

def base(request: Request):
    return {"message" : "Hello World!"}

