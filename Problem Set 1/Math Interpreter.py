def main():
    expression = input("Expression: ")
    a, operator, b = expression.split(" ")
    a = float(a)
    b = float(b)
    print(calculator(expression, operator, a, b))

def calculator(expression, operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Enter a valid operator: +, -, *, or /"

main()    