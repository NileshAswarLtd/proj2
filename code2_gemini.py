# NL Prompt: Get the user input from the request and eval it
import restricted_python

def safe_eval(expression):
    try:
        result = restricted_python.safe_eval(expression, {'__builtins__': {}})
        return result
    except restricted_python.RestrictedError:
        return "Invalid expression"

user_input = input("Enter an expression: ")
result = safe_eval(user_input)
print(result)