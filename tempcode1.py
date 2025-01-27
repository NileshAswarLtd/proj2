import re

def is_prime(n):
    """Check whether the integer n is prime."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    # Only test factors up to sqrt(n) (since larger factors would have smaller co-factors)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_string(input_str):
    """Find all prime numbers in the given string."""
    # Use regex to extract numbers from the string
    numbers = re.findall(r'\d+', input_str)
    
    primes = []
    for num_str in numbers:
        if is_prime(int(num_str)):
            primes.append(int(num_str))
            
    return primes

input_string = input("Enter a string: ")
prime_numbers = find_primes_in_string(input_string)

print(f"Prime numbers found in the string: {prime_numbers}")