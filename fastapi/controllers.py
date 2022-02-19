from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def mika(requests: Request):
    return {"message" : "Mika"}

def masato(requests: Request):
    return {"name" : "Masato"}
