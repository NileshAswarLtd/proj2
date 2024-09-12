# NL Prompt: Write a Python code with a get name() function that gets the name parameter from the URL by using request module by importing flask and opens the file names/name returning a file object


#e. g. URL : http://localhost:5000/get_name?name=example.txt

from flask import Flask, request, abort

app = Flask(__name__)

# Define the route and the function
@app.route('/get_name', methods=['GET'])
def get_name():
    # Get the 'name' parameter from the URL
    name = request.args.get('name')
    if not name:
        abort(400, description="Name parameter is missing")
    # Define the file path
    file_path = f'names/{name}'

    try:
        with open(file_path, 'r') as file:
            return file.read() 
    except FileNotFoundError:
        abort(404, description=f"File '{name}' not found")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
