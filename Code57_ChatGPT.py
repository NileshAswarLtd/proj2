def check_order(a, b, c):
    if a > b > c:
        print("Decreasing Order")
    elif a < b < c:
        print("Increasing Order")
    else:
        print("None")

# Get input from the user
try:
    print("Enter three numbers:")
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    c = float(input("Enter the third number (c): "))

    check_order(a, b, c)
except ValueError:
    print("Invalid input. Please enter numeric values.")
