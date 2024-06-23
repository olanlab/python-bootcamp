import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raises an HTTPError for non-200 status codes
    print(response.text)
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.ConnectionError:
    print("Failed to establish a connection.")
except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    print("An error occurred:", e)
