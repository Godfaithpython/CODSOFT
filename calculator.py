def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():
    print("===== Simple Calculator =====")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Select operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the desired operation (+/-/*//): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation.")
        return

    print(f"{num1} {operation} {num2} = {result}")

calculate()