from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def base(request: Request):
    return {"message" : "Hello World!"}

def one(request: Request):
    return 1

def two(request: Request):
    return 2

def three(request: Request):
    return 3
