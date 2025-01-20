# app/repositories/user_repository.py

# Custom exception for repository errors
class UserRepositoryError(Exception):
    pass

users_db = {}

def save_user(user):
    try:
        # Try saving the user
        if user.id in users_db:
            # If the user already exists, raise a custom exception
            raise UserRepositoryError("User already exists")
        users_db[user.id] = user
        return user
    except UserRepositoryError as e:
        # Catch and re-raise the repository-specific exception
        raise UserRepositoryError(f"Failed to save user: {str(e)}")
    except Exception as e:
        # Catch any unexpected error and re-raise it
        raise Exception(f"Unexpected error while saving user: {str(e)}")

def fetch_user_by_id(user_id):
    try:
        # Try fetching the user by ID
        if user_id not in users_db:
            # If the user does not exist, raise a custom exception
            raise UserRepositoryError("User not found")
        return users_db[user_id]
    except UserRepositoryError as e:
        # Catch and re-raise the repository-specific exception
        raise UserRepositoryError(f"Failed to fetch user: {str(e)}")
    except Exception as e:
        # Catch any unexpected error and re-raise it
        raise Exception(f"Unexpected error while fetching user: {str(e)}")
