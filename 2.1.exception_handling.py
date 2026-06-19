# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
    
# except ValueError:
#     print("Use numbers only")
# except ZeroDivisionError:
#     print("A number can't be divided by zero")

# else:
#     print(result)

# finally:
#     print("Process completed successfully")

try:
    with open("file.txt", "r") as file:
        details = file.read()
        print(details)
except FileNotFoundError:
    print("File was not found")