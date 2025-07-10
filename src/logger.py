import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file name with timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,  # Use DEBUG, WARNING, ERROR as needed
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


logger = logging.getLogger()
