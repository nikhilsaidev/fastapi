# app/controllers/user_controller.py
from fastapi import APIRouter, HTTPException
from app.services.user_service import create_user, get_user
from app.models.user_model import User

router = APIRouter()

@router.post("/")
def add_user(user: User):
    try:
        # Try to create a user using the service layer
        return create_user(user)
    except ValueError as e:
        # Catch specific exceptions, e.g., user already exists, and raise HTTPException
        raise HTTPException(status_code=400, detail=f"Value error: {str(e)}")
    except Exception as e:
        # Catch any other unexpected errors and raise HTTPException
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{user_id}")
def fetch_user(user_id: str):
    try:
        # Try to fetch a user by ID using the service layer
        return get_user(user_id)
    except ValueError as e:
        # If the user is not found or any other value error occurs
        raise HTTPException(status_code=404, detail=f"User not found: {str(e)}")
    except Exception as e:
        # Catch any other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
