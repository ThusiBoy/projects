def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's your first number? "))
    for symbol in operations:
        print(symbol)

    done_calculating = True
    while done_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's your next number? "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        keep_calculating = (input(f"Type 'y' to continue calculating with {answer} or Type 'no' to start"))
        if keep_calculating == "y":
            num1 = answer
        else:
            done_calculating = False
            calculator()

calculator()