#!/usr/bin/python3
"""Module contains text-indentation function."""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:\
 ., ? and :.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    strlen = len(text)
    c = 0
    while c < strlen and text[c] in " \t":
        c += 1
    while c < strlen:
        print(text[c], end="")
        if text[c] == "\n" and c != strlen - 1:
            c += 1
            while c < strlen and text[c] in " \t":
                c += 1
            continue
        else:
            if text[c] in ".?:":
                print("\n")
                c += 1
                if c < strlen and text[c] == "\n":
                    print('')
                    c += 1
                while c < strlen and text[c] in " \t":
                    c += 1
                continue
        c += 1
