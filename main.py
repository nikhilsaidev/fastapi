from fastapi import FastAPI
from app.middleware.log_middleware import LogMiddleware
from app.middleware.error_handler import ErrorHandler
from app.controllers.user_controller import router as user_router

app = FastAPI(title="User Management API")

# Add middleware for logging and error handling
app.add_middleware(LogMiddleware)
app.add_exception_handler(Exception, ErrorHandler.handle_exception)

# Include user-related routes
app.include_router(user_router, prefix="/users", tags=["Users"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=5000)
