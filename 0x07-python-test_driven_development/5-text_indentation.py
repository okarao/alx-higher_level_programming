#!/usr/bin/python3
# 5-text_indentation.py
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Helper function to skip spaces and newline characters
    def skip_spaces_and_newlines(start):
        i = start
        while i < len(text) and (text[i] == ' ' or text[i] == '\n'):
            i += 1
        return i

    c = skip_spaces_and_newlines(0)

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n\n", end="")
            c = skip_spaces_and_newlines(c + 1)
        else:
            c += 1
