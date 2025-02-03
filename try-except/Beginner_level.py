try:
    age = int(input("Enter your age: "))  # Converts input to integer
    print(f"You are {age} years old.")
except ValueError:  # Handles invalid input (e.g., "abc")
    print("Invalid input! Please enter a valid number.")
    