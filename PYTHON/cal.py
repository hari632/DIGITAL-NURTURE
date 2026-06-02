def calculate(a, b, op):

    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":
        return a / b

    else:
        return "Invalid Operator"


try:

    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    op = input("Enter Operator (+,-,*,/): ")

    result = calculate(a, b, op)

    print(f"Result = {result}")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid numeric values")