from fastapi import FastAPI
from endpoints.routes import router as delivery_router
import uvicorn


app = FastAPI()

app.include_router(delivery_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


