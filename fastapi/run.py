from urls import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app=app, host="192.168.3.21", port=8000)
