from app.utils.helpers import LoggerHelper


logger = LoggerHelper.get_logger("UserRepository")

# Custom exception for repository errors
class UserRepositoryError(Exception):
    pass

users_db = {}

def save_user(user):
    try:
        logger.info(f"Attempting to save user: {user.id}")
        # Try saving the user
        if user.id in users_db:
            logger.warning(f"User already exists with ID: {user.id}")
            raise UserRepositoryError("User already exists")
        users_db[user.id] = user
        logger.info(f"User saved successfully: {user.id}")
        return user
    except UserRepositoryError as e:
        logger.error(f"Failed to save user: {user.id} - {str(e)}")
        raise UserRepositoryError(f"Failed to save user: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error while saving user: {user.id} - {str(e)}", exc_info=True)
        raise Exception(f"Unexpected error while saving user: {str(e)}")

def fetch_user_by_id(user_id):
    try:
        logger.info(f"Attempting to fetch user by ID: {user_id}")
        # Try fetching the user by ID
        if user_id not in users_db:
            logger.warning(f"User not found with ID: {user_id}")
            raise UserRepositoryError("User not found")
        logger.info(f"User fetched successfully: {user_id}")
        return users_db[user_id]
    except UserRepositoryError as e:
        logger.error(f"Failed to fetch user: {user_id} - {str(e)}")
        raise UserRepositoryError(f"Failed to fetch user: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error while fetching user: {user_id} - {str(e)}", exc_info=True)
        raise Exception(f"Unexpected error while fetching user: {str(e)}")
