import re

# Token types (regular expressions)
TOKEN_TYPES = {
    'KEYWORD': r'\b(if|else|while|for|int|float)\b',
    'FLOAT': r'\b\d+\.\d+\b',
    'INTEGER': r'\b\d+\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'OPERATOR': r'==|!=|>=|<=|[+\-*/=<>]',
    'SEPARATOR': r'[(){}\[\];,]',
}

# Token class
class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f'Token({self.token_type}, {self.value})'

# Lexical analyzer class
class LexicalAnalyzer:
    def __init__(self, code):
        self.code = code
        self.index = 0
        self.tokens = []

    def analyze(self):
        while self.index < len(self.code):
            char = self.code[self.index]

            # Skip whitespace
            if char.isspace():
                self.index += 1
                continue

            # Try matching each token type
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.code, self.index)
                if match:
                    value = match.group()
                    self.tokens.append(Token(token_type, value))
                    self.index = match.end()
                    break
            else:
                raise SyntaxError(f'Invalid character: {char}')

        return self.tokens


# Main program for testing
if __name__ == "__main__":
    # Sample mini-program
    code = """
    int x = 10;
    float y = 3.14;
    if (x > y) {
        x = x + 1;
    } else {
        y = y - 1;
    }
    """

    lexer = LexicalAnalyzer(code)
    tokens = lexer.analyze()

    print("Tokens:")
    for token in tokens:
        print(token)