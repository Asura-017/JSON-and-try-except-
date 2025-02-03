import logging

# Configure logging
logging.basicConfig(filename="app_errors.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    result = 10 / 0  # Division by zero error
except ZeroDivisionError as e:
    logging.error(f"ZeroDivisionError occurred: {e}")  # Logs error instead of printing
    print("Oops! Something went wrong. The error has been logged.")
