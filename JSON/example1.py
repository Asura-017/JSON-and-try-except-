import json

# Example: User data stored as JSON
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "is_active": True,
    "roles": ["admin", "editor"]
}

# Converting Python dictionary to JSON string (serialization)
json_data = json.dumps(user_data, indent=4)
print("JSON Formatted Data:\n", json_data)

# Simulating saving JSON data to a file
with open("user_data.json", "w") as file:
    file.write(json_data)

# Reading JSON data from a file (deserialization)
with open("user_data.json", "r") as file:
    loaded_data = json.load(file)

print("\nLoaded Data from JSON File:\n", loaded_data)
