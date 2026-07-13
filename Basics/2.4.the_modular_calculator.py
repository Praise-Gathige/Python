def add(a,b):
    result = a + b
    print(f"Result: {result}")

def subtract(a,b):
    result = a - b
    print(f"Result: {result}")

def multiply(a,b):
    result = a * b
    print(f"Result: {result}")

def divide(a,b):
    if b == 0:
        print("Cannot divide by zero!")
    else:
        result = a / b
        print(f"Result: {result}")


while True:
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Quit")
    user_input = input("Enter your choice: ")

    if user_input == "5":
        break

    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))

    if user_input == "1":
        add(num1, num2)
    elif user_input == "2":
        subtract(num1, num2)
    elif user_input == "3":
        multiply(num1, num2)
    elif user_input == "4":
        divide(num1, num2)
    else:
        print("Invalid choice. Please select 1-5.")