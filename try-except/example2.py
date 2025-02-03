try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2  # Risky operation (division by zero)
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
