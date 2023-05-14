from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.routes import router as delivery_router
import uvicorn


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(delivery_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

