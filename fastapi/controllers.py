from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def index(requests: Request):
    return {"message" : "Hello"}
