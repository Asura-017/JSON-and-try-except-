try:
    file = open("data.txt", "r")  # Trying to open a file
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Ensures the file is always closed
