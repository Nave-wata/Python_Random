from fastapi import FastAPI
from starlette.requests import Request

import datetime

app = FastAPI()

def base(request: Request):
    return {"message" : "Hello World!"}

def one(request: Request):
    time = datetime.datetime.now()
    return {"Now" : time}
