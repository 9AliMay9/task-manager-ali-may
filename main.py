from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routes import router as task_router
from token_issuer import router as token_router

app = FastAPI()

# Include the task router
app.include_router(task_router, prefix="/tasks")
# Include the token router
app.include_router(token_router, prefix="/auth")


@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the Task Manager API!"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Handle HTTPException globally.
    Returns JSON response with error details and status code.
    """
    return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                "message": exc.detail,
                "status_code": exc.status_code,
                "type": "HTTPException"
            })
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    Handle unexpected exceptions globally.
    Returns a generic 500 JSON error response.
    """
    return JSONResponse(
            status_code=500,
            content=jsonable_encoder({
                "message": "An unexpected error occurred.",
                "status_code": 500,
                "type": "GeneralException"
            })
    )
