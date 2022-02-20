from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def base(request: Request):
    return {"message" : "Hello World!"}

def one(request: Request):
    return {"Number" : 1}

def two(request: Request):
    return {"Number" : 2}

def three(request: Request):
    return {"Number" : 3}
