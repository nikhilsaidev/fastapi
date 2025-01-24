import uuid
import logging
from logging.handlers import RotatingFileHandler
import os

def generate_user_id():
    return str(uuid.uuid4())


class LoggerHelper:
    """
    Helper class for configuring and providing loggers.
    """

    @staticmethod
    def setup_logging(log_dir="logs", log_file="app.log", max_bytes=5 * 1024 * 1024, backup_count=3):
        """
        Set up logging configuration.

        :param log_dir: Directory to store log files.
        :param log_file: Name of the log file.
        :param max_bytes: Maximum size of a log file before rotation.
        :param backup_count: Number of backup log files to keep.
        """
        # Ensure the log directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Log file path
        log_file_path = os.path.join(log_dir, log_file)

        # Configure rotating file handler
        file_handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(logging.INFO)

        # Configure console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Set the logging format
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=log_format, handlers=[file_handler, console_handler])

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Get a logger instance with the specified name.

        :param name: Name of the logger (usually the module name).
        :return: Configured logger instance.
        """
        return logging.getLogger(name)

# Example of setting up the logger (should be called once in the main entry point of the application)
LoggerHelper.setup_logging()
