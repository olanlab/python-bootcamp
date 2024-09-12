import os
import logging

dirname, filename = os.path.split(os.path.abspath(__file__))

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{dirname}/example.log"),  # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Log messages with different severity levels
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")
