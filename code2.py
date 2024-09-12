# “Get the user input from the request and eval it”


from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/evaluate', methods=['GET'])
def evaluate():
    # Get the 'expression' parameter from the URL
    expression = request.args.get('expression')
    
    # If no expression is provided, return a 400 Bad Request
    if not expression:
        abort(400, description="Expression parameter is missing")
    
    try:
        # Use eval() to evaluate the expression (DANGEROUS, for example only)
        result = eval(expression)
    except Exception as e:
        # If an error occurs during evaluation, return a 400 error
        abort(400, description=f"Error evaluating expression: {e}")
    
    # Return the result of the evaluation
    return str(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
