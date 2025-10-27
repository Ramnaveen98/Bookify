from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(title="Bookify", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to Bookify!"}
