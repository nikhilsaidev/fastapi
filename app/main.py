from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.utils.helpers import LoggerHelper

app = FastAPI(title="User Management API")

LoggerHelper.setup_logging()


# Include user-related routes
app.include_router(user_router, prefix="/users", tags=["Users"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=5000)
