def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if (b == 0):
        print("Division not possible")
    else:
        return a/b


num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operator = str(input("Enter operator( + , - , * , / ):"))
if (operator == "+"):
    print(add(num1, num2))
elif (operator == "-"):
    print(sub(num1, num2))
elif (operator == "*"):
    print(mul(num1, num2))
elif (operator == "/"):
    if div(num1, num2) is not None:
        print(div(num1, num2))
else:
    print("Invalid input!")
