import logging
import os
from logging.handlers import RotatingFileHandler

dirname, filename = os.path.split(os.path.abspath(__file__))

# Configure logging
handler = RotatingFileHandler(f"{dirname}/rotating_example.log", maxBytes=2000, backupCount=5)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        handler,
        logging.StreamHandler()
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Log messages to demonstrate rotation
for i in range(100):
    logger.debug(f"Log message {i}")
