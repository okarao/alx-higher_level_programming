#!/usr/bin/python3
"""
This module contains a function text_indentation that prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    :param text: The input text
    :type text: str
    :raises TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    new_text = ''
    for char in text:
        new_text += char
        if char in punctuations:
            new_text += '\n\n'
    
    # Remove extra newlines at the end
    new_text = new_text.rstrip('\n')
    
    print(new_text)

if __name__ == "__main__":
    example_text = "This is a sample text. It contains some punctuation: like dots. And question marks? Also, colons: for separation."
    text_indentation(example_text)
