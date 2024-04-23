import re

def lexer(input_string):
    operators = ['+', '-', '*', '/', '=', '<', '>', '==', '!=', '<=', '>=', '&&', '||', '!', '&', '|']
    tokens = re.findall(r'[-+*/=<>!&|]+', input_string)
    for token in tokens:
        if token in operators:
            print(f'{token}: operator')

# Example usage:
input_string = input("Enter code: ")
lexer(input_string)