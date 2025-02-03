import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raises an error for HTTP errors (e.g., 404, 500)
    data = response.json()  # Convert response to JSON
    print("Data received:", data)
except requests.exceptions.ConnectionError:
    print("Network error! Please check your internet connection.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
