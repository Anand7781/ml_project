import logging
import os
from datetime import datetime

# Create filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Directory to store logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensure the directory exists
os.makedirs(logs_dir, exist_ok=True)

# Full path to log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log file created at: {LOG_FILE_PATH}")
