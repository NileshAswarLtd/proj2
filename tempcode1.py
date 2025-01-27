def is_prime(n):
  """
  Checks if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_primes_in_string(s):
  """
  Finds and prints all prime numbers within a string.

  Args:
    s: The input string.
  """
  primes = []
  for word in s.split():
    try:
      num = int(word)
      if is_prime(num):
        primes.append(num)
    except ValueError:
      pass  # Skip non-numeric words

  if primes:
    print("Prime numbers found in the string:")
    for prime in primes:
      print(prime)
  else:
    print("No prime numbers found in the string.")

# Interactive part
while True:
  try:
    n = int(input("Enter a number to check for primality (or 'q' to quit): "))
    if n == 'q':
      break
    if is_prime(n):
      print(f"{n} is a prime number.")
    else:
      print(f"{n} is not a prime number.")

    s = input("Enter a string to find prime numbers in: ")
    find_primes_in_string(s)
  except ValueError:
    print("Invalid input. Please enter an integer or 'q' to quit.")