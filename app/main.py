from fastapi import FastAPI

import app
from app.controller import personDetailsController
from app.db.base import Base
from app.db.session import engine


# Create FastAPI instance
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookify", version="1.0.0")
app.include_router(
    personDetailsController.router,
    prefix="/api/v1/person",
    tags=["Person"]
)



@app.get("/")
def root():
    return {"message": "Welcome to Bookify!"}
