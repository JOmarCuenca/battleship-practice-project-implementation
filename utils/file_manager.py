import os
from . import logger

class FileManager:
    @staticmethod
    def check_and_create_directory(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logger.debug(f"Directory '{directory_path}' created.")
        else:
            logger.debug(f"Directory '{directory_path}' already exists.")
