# app/services/user_service.py
from app.repositories.user_repository import save_user, fetch_user_by_id
from app.models.user_model import User
from app.repositories.user_repository import UserRepositoryError

def create_user(user: User):
    try:
        # Try saving the user in the repository
        return save_user(user)
    except UserRepositoryError as e:
        # If repository raises a custom exception (e.g., user already exists)
        raise ValueError(f"Error in creating user: {str(e)}")
    except Exception as e:
        # If something else goes wrong in the service layer
        raise Exception(f"Service layer error: {str(e)}")

def get_user(user_id: str):
    try:
        # Try to fetch the user by ID
        return fetch_user_by_id(user_id)
    except UserRepositoryError as e:
        # Handle repository-specific error
        raise ValueError(f"Error in fetching user: {str(e)}")
    except Exception as e:
        # Catch any other service-related errors
        raise Exception(f"Service layer error: {str(e)}")
