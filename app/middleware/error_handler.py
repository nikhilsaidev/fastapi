# app/middlewares/error_handler.py
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request

class ErrorHandler:
    @staticmethod
    def handle_exception(request: Request, exc: Exception):
        # Handle general exceptions that are not specifically caught elsewhere
        if isinstance(exc, RequestValidationError):
            return JSONResponse(
                status_code=422,
                content={"message": "Validation error", "details": exc.errors()}
            )
        return JSONResponse(
            status_code=500,
            content={"message": str(exc)}
        )
