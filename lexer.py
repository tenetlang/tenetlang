import re
from collections import namedtuple



# Define the token types
Token = namedtuple('Token', ['type', 'value', 'line', 'column'])

# Define the token patterns
token_patterns = [
    ('WHITESPACE', r'\s+'),
    ('COMMENT', r'//.*'),
    ('IDENTIFIER', r'[^\W\d]\w*'),
    ('NUMBER', r'\d+'),
    ('STRING', r'"(?:[^"\\]|\\.)*"'),
    ('CLASS', r'class'),
    ('LET', r'let'),
    ('FUNCTION', r'function'),
    ('ASYNC', r'async'),
    ('RETURN', r'return'),
    ('AWAIT', r'await'),
    ('FOR', r'for'),
    ('IN', r'in'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('COLON', r':'),
    ('SEMICOLON', r';'),
    ('ARROW', r'->'),
    ('FATARROW', r'=>'),
    ('EQUAL', r'='),
    ('OPERATOR', r'[-+*/%&|<>!]=?'),
]

# Compile the token patterns
token_patterns = [(name, re.compile(pattern)) for name, pattern in token_patterns]

def tokenize(code):
    tokens = []
    line_number = 1
    column_number = 1

    while code:
        matched = False

        for token_name, token_pattern in token_patterns:
            match = token_pattern.match(code)

            if match:
                value = match.group(0)
                tokens.append(Token(token_name, value, line_number, column_number))

                # Update line and column numbers
                line_number += value.count('\n')
                column_number = len(value) - value.rfind('\n')

                # Update the code
                code = code[len(value):]
                matched = True
                break

        if not matched:
            raise SyntaxError(f"Unexpected character at line {line_number}, column {column_number}")

    return tokens

# Test the lexer with the example code
code = '''
# Insert the provided code snippet here
'''

tokens = tokenize(code)
for token in tokens:
    print(token)
