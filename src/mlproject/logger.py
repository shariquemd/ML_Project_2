import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging_str = "[%(asctime)s:%(levelname)s: %(module)s:%(message)s]"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=logging_str,  # Corrected format argument
    level=logging.INFO,
)


