from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

def masao(request: Request):
    return {"name" : "Masao\\n",
            "my-" : "father\\n"}

def mika(requests: Request):
    return {"message" : "Mika\\n",
            "my-" : "mother\\n"}

def masato(requests: Request):
    return {"name" : "Masato\\n",
            "my-": "\\n"}
