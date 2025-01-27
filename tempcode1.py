import re

def reverse_words_with_punctuation(text):
    """
    Reverses the order of words with punctuation and keeps the punctuation in place.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The processed text with reversed word order.
    """
    # Remove punctuation
    no_punct = re.sub(r'[^\w\s]', '', text)

    # Reverse words
    reversed_no_punct = ' '.join(reversed(no_punct.split()))

    return reversed_no_punct

# Test the function
text = input("Enter a string: ")
print("Processed Text:", reverse_words_with_punctuation(text))
