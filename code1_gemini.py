# Write a Python code with a get name() function that gets the name parameter from the URL by using request module by importing flask and opens the file names/name returning a file object

from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route('/get_name/<string:name>')
def get_name(name):
    # Get the name parameter from the URL
    name_from_url = name

    # Construct the file path
    file_path = f'names/{name_from_url}'

    # Open the file and return its contents
    try:
        with open(file_path, 'rb') as f:
            return send_file(f)
    except FileNotFoundError:
        return "File not found.", 404

if __name__ == '__main__':
    app.run(debug=True)