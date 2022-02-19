from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def base(request: Request):
    return {"message" : "Hello World!"}

def one(request: Request):
    a: int = 1
    return {"Number" : {a}}
