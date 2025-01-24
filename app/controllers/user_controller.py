from fastapi import APIRouter, HTTPException
from app.services.user_service import create_user, get_user
from app.models.user_model import User
from app.utils.helpers import LoggerHelper
import logging

# Configure logging
logger = LoggerHelper.get_logger("UserController")


router = APIRouter()

@router.post("/")
def add_user(user: User):
    try:
        logger.info(f"Received request to add user: {user}")
        # Try to create a user using the service layer
        result = create_user(user)
        logger.info(f"Successfully added user: {user.id}")
        return result
    except ValueError as e:
        logger.warning(f"Value error while adding user {user.id}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Value error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error while adding user {user.id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{user_id}")
def fetch_user(user_id: str):
    try:
        logger.info(f"Received request to fetch user with ID: {user_id}")
        # Try to fetch a user by ID using the service layer
        result = get_user(user_id)
        logger.info(f"Successfully fetched user: {user_id}")
        return result
    except ValueError as e:
        logger.warning(f"User not found with ID {user_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=f"User not found: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error while fetching user {user_id}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
