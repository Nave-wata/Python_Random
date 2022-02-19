from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def base(request: Request):
    return {"message" : "Hello World!"}

def masao(request: Request):
    return {"name" : "Masao",

            "my-" : "father"}

def mika(requests: Request):
    return {"message" : "Mika",
            "my-" : "mother"}

def masato(requests: Request):
    return {"name" : "Masaton",
            "my-": ""}
