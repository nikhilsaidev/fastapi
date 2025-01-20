from starlette.middleware.base import BaseHTTPMiddleware
import logging

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Log the incoming request
        logging.info(f"Request: {request.method} {request.url}")
        
        # Call the next middleware or route handler
        response = await call_next(request)
        
        # Log the response status
        logging.info(f"Response status: {response.status_code}")
        
        return response
