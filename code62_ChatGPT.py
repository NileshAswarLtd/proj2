from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reverse Words with Punctuation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
            text-align: center;
        }
        textarea {
            width: 80%;
            height: 100px;
            margin-bottom: 20px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Reverse Words with Punctuation</h1>
    <form method="POST">
        <textarea name="text" placeholder="Enter your text here...">{{ input_text }}</textarea><br>
        <button type="submit">Reverse Words</button>
    </form>
    {% if output_text is not none %}
        <h2>Reversed Text:</h2>
        <p>{{ output_text }}</p>
    {% endif %}
</body>
</html>
"""

def reverse_words_with_punctuation(text):
    words = [word for word in text.split() if word.isalnum()]
    result = []
    word_index = len(words) - 1

    for char in text.split():
        if char.isalnum():
            result.append(words[word_index])
            word_index -= 1
        else:
            result.append(char)

    return ' '.join(result)

@app.route('/', methods=['GET', 'POST'])
def reverse_words():
    input_text = ""
    output_text = None

    if request.method == 'POST':
        input_text = request.form['text']
        output_text = reverse_words_with_punctuation(input_text)

    return render_template_string(HTML_TEMPLATE, input_text=input_text, output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
