 # app/main.py
from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Simple FastAPI App")

# Include routes
app.include_router(router)

# Run the server using: uvicorn app.main:app --reload
