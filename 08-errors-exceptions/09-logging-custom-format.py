import logging
import os
from logging.handlers import TimedRotatingFileHandler

dirname, filename = os.path.split(os.path.abspath(__file__))

# Configure logging
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set up a timed rotating file handler
log_file = f"{dirname}/timed_example.log"
handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7)
handler.setFormatter(log_formatter)
handler.suffix = "%Y-%m-%d"  # Add date suffix to the log files

# Configure the root logger
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler, logging.StreamHandler()]
)

# Create a logger
logger = logging.getLogger(__name__)

# Log some messages to demonstrate rotation
logger.info("This is an INFO message")
logger.debug("This is a DEBUG message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

# Log messages in a loop to simulate continuous logging
import time
for i in range(100):
    logger.info(f"Log message {i}")
    time.sleep(1)
