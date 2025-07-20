from fastapi import FastAPI
from routes import router as task_router

app = FastAPI()

# Include the task router from routes.py
app.include_router(task_router, prefix="/tasks")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}
