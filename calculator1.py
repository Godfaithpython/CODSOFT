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

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice (1/2/3/4): ")

    if operation == '1':
        result = add(num1, num2)
        operator = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif operation == '4':
        result = divide(num1, num2)
        operator = '/'
    else:
        print("Invalid operation choice.")
        return

    print(f"{num1} {operator} {num2} = {result}")

calculate()