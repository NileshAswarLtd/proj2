# NL Prompt: Get the user input from the request and eval it.


from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/evaluate', methods=['GET'])
def evaluate():
    # Get the 'expression' parameter from the URL
    expression = request.args.get('expression')
    
     if not expression:
        abort(400, description="Expression parameter is missing")
    
    try:
        result = eval(expression)
    except Exception as e:
        abort(400, description=f"Error evaluating expression: {e}")
    
    # Return the result of the evaluation
    return str(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
