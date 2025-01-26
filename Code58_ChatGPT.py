import math

def quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the number of solutions based on the discriminant
    if discriminant < 0:
        print("Complex Roots")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Single solution: {root}")
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f"Two solutions: {root1}, {root2}")

# Get coefficients from the user
try:
    print("For the quadratic equation ax^2 + bx + c = 0:")
    a = float(input("Enter the coefficient a (non-zero): "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    if a == 0:
        print("The coefficient 'a' cannot be zero for a quadratic equation.")
    else:
        quadratic_roots(a, b, c)
except ValueError:
    print("Invalid input. Please enter numeric values.")
