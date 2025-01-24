import logging
from app.repositories.user_repository import save_user, fetch_user_by_id
from app.models.user_model import User
from app.repositories.user_repository import UserRepositoryError
from app.utils.helpers import LoggerHelper

logger = LoggerHelper.get_logger("UserService")

def create_user(user: User):
    try:
        logger.info(f"Service layer: Creating user {user.id}")
        # Try saving the user in the repository
        result = save_user(user)
        logger.info(f"User created successfully: {user.id}")
        return result
    except UserRepositoryError as e:
        logger.warning(f"Repository error while creating user {user.id}: {str(e)}")
        raise ValueError(f"Error in creating user: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in service layer while creating user {user.id}: {str(e)}", exc_info=True)
        raise Exception(f"Service layer error: {str(e)}")

def get_user(user_id: str):
    try:
        logger.info(f"Service layer: Fetching user {user_id}")
        # Try to fetch the user by ID
        result = fetch_user_by_id(user_id)
        logger.info(f"User fetched successfully: {user_id}")
        return result
    except UserRepositoryError as e:
        logger.warning(f"Repository error while fetching user {user_id}: {str(e)}")
        raise ValueError(f"Error in fetching user: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in service layer while fetching user {user_id}: {str(e)}", exc_info=True)
        raise Exception(f"Service layer error: {str(e)}")
