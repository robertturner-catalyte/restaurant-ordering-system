from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Restaurant Ordering System is running!"}