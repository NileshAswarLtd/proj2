def interactive_calculator():
    print("Welcome to the Interactive Calculator!")
    print("Select an operation by entering the corresponding number:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Integer Division")
    print("6 - Modulo")

    try:
        operation = int(input("Enter your choice (1-6): "))
        if operation not in [1, 2, 3, 4, 5, 6]:
            print("Please choose a valid operation.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 4 and num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        elif operation == 5 and num2 == 0:
            print("Error: Integer division by zero is not allowed.")
            return
        elif operation == 6 and num2 == 0:
            print("Error: Modulo by zero is not allowed.")
            return

        if operation == 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == 4:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        elif operation == 5:
            result = num1 // num2
            print(f"{num1} // {num2} = {result}")
        elif operation == 6:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
interactive_calculator()
