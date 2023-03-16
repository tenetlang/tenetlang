import re
from collections import namedtuple


# Define the token types
Token = namedtuple('Token', ['type', 'value', 'line', 'column'])

# Define token
token_patterns = [
    ('WHITESPACE', r'\s+'),
    ('COMMENT', r'//.*'),
    ('NUMBER', r'\d+(\.\d*)?([eE][+-]?\d+)?'),
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
    ('NOT_EQUAL', r'!='),
    ('EQUAL_EQUAL', r'=='),
    ('NOT_EQUAL_EQUAL', r'!=='),
    ('LESS_THAN', r'<'),
    ('LESS_THAN_EQUAL', r'<='),
    ('GREATER_THAN', r'>'),
    ('GREATER_THAN_EQUAL', r'>='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('MODULUS', r'%'),
    ('POWER', r'\*\*'),
    ('INCREMENT', r'\+\+'),
    ('DECREMENT', r'--'),
    ('LOGICAL_AND', r'&&'),
    ('LOGICAL_OR', r'\|\|'),
    ('BITWISE_AND', r'&'),
    ('BITWISE_OR', r'\|'),
    ('BITWISE_XOR', r'\^'),
    ('BITWISE_NOT', r'~'),
    ('LEFT_SHIFT', r'<<'),
    ('RIGHT_SHIFT', r'>>'),
    ('UNSIGNED_RIGHT_SHIFT', r'>>>'),
    ('ASSIGN_ADD', r'\+='),
    ('ASSIGN_SUB', r'-='),
    ('ASSIGN_MUL', r'\*='),
    ('ASSIGN_DIV', r'/='),
    ('ASSIGN_MOD', r'%='),
    ('ASSIGN_POW', r'\*\*='),
    ('ASSIGN_LSHIFT', r'<<='),
    ('ASSIGN_RSHIFT', r'>>='),
    ('ASSIGN_URSHIFT', r'>>>='),
    ('ASSIGN_BAND', r'&='),
    ('ASSIGN_BOR', r'\|='),
    ('ASSIGN_BXOR', r'^='),
    ('IMPORT', r'import'),
    ('SUGGEST', r'suggest'),
    ('SUGGEST_COMPLETE', r'complete'),
    ('SUGGEST_DOCUMENT', r'document'),
    ('SUGGEST_REFACTOR', r'refactor'),
    ('IDENTIFIER', r'[^\W\d]\w*'),
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

# Open file
tenet_sample_file = open("./sample.tnt", "r")

#read whole file to a string
tenet_sample_code_str = tenet_sample_file.read()

#close file
tenet_sample_file.close()

tokens = tokenize(tenet_sample_code_str)
for token in tokens:
    print(token)
