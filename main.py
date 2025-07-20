from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routes import router as task_router

app = FastAPI()

# Include the task router from routes.py
app.include_router(task_router, prefix="/tasks")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}


# Global exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                "message": exc.detail,
                "status_code": exc.status_code,
                "type": "HTTPException"
            })
    )


# Global exception handler for unexpected errors
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
            status_code=500,
            content=jsonable_encoder({
                "message": "An unexpected error occurred.",
                "status_code": 500,
                "type": "GeneralException"
            })
    )
