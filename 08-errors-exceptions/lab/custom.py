class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print("Custom error:", e)
except Exception as e:
    print("An error occurred:", e)
