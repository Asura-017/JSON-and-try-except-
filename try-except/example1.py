num = int(input("Enter a number: "))  # If user enters "abc", program crashes
print("You entered:", num)
try:
    num = int(input("Enter a number: "))  # Tries to convert input to integer
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")
