"""Smart Calculator - a small command-line calculator.

Project for the UCS745 Cloud and DevOps lab (Git and GitHub assignment).
Type an expression such as  12 / 4  and the result is printed.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b, places=2):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return round(a / b, places)


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(expression):
    """Evaluate 'number operator number', for example '12 / 4'."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("use the format: number operator number, e.g. 12 / 4")
    a, op, b = parts
    if op not in OPERATIONS:
        raise ValueError("unknown operator '%s', use one of + - * /" % op)
    return OPERATIONS[op](float(a), float(b))


def main():
    print("Smart Calculator (type 'exit' to quit)")
    while True:
        try:
            expression = input("calc> ").strip()
        except EOFError:
            break
        if expression.lower() == "exit":
            break
        try:
            print("=", calculate(expression))
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
