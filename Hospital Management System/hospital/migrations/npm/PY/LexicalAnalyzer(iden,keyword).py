import re

def lexer(input_string):
    keywords = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}
    tokens = re.findall(r'\b\w+\b', input_string)
    for token in tokens:
        if token in keywords:
            print(f'{token}: keyword')
        else:
            print(f'{token}: identifier')

# Example usage:
input_string = input("Enter code: ")
lexer(input_string)