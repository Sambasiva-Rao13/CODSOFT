# Simple Calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operation (+, -, *, /): ")
    
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = sub(num1, num2)
    elif op == "*":
        result = mul(num1, num2)
    elif op == "/":
        result = div(num1, num2)
    else:
        print("Invalid operation!")
        continue

    print(f"Result: {result:.2f}")