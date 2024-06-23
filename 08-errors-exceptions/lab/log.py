
import logging
import os

dirname, filename = os.path.split(os.path.abspath(__file__))


# Configure logging
logging.basicConfig(filename=f"{dirname}/app.log", level=logging.ERROR)

def process_data(data):
    try:
        # Perform some data processing
        result = data / 0  # Simulating a division by zero error
    except ZeroDivisionError as e:
        logging.error("Division by zero error: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    try:
        data = int(input("Enter a number: "))
        process_data(data)
    except ValueError:
        print("Please enter a valid number.")
