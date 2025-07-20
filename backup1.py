import re

# Token definitions for Nepali
TOKENS_NEPALI = [
    # Keywords
    ('IF', r'Yedi'),
    ('ELSE', r'Athawa'),
    ('ELSE_IF', r'Yo\ Athawa'),
    ('WHILE', r'Jabasamma'),
    ('FOR', r'Kolagi'),
    ('RETURN', r'Farkau'),
    ('FUNCTION', r'Karyakram'),
    ('PRINT', r'Dekhau'),
    ('INPUT', r'Linuhoos'),
    ('TRUE', r'Sahi'),
    ('FALSE', r'Galat'),
    ('AND', r'Ra'),
    ('OR', r'Wa'),
    ('NOT', r'Hoina'),
    ('BREAK', r'rokdinus'),
    ('CONTINUE', r'chalos'),
    ('SWITCH', r'Pariwartan'),
    ('CASE', r'Sthiti'),
    ('DEFAULT', r'hoinava'),

    # Data Types
    ('TYPE', r'(anka|Dashanka|Shabda|Akshar|Satya|Suchi|Shabdakosh|Khali|Ganna|Sanrachana)'),

    # Symbols
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('ASSIGN', r'\='),
    ('COMMA', r','),

    # Operators
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('MODULO', r'%'),

    # Relational Operators
    ('LT', r'<'),
    ('GT', r'>'),
    ('LE', r'<='), 
    ('GE', r'>='), 
    ('EQ', r'=='),
    ('NEQ', r'!='),

    # Literals
    ('NUMBER', r'\d+'),
    ('STRING_LITERAL', r'\".*?\"'),

    # Identifiers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),

    # Comments
    ('COMMENT', r'//.*'),

    # Whitespace (ignored)
    ('WHITESPACE', r'\s+'),

    # Unknown
    ('UNKNOWN', r'.'),
]

class LexerNepali:
    def __init__(self, token_definitions):
        self.token_specification = [(name, re.compile(pattern)) for name, pattern in token_definitions]

    def tokenize(self, code):
        tokens = []
        pos = 0
        while pos < len(code):
            for name, pattern in self.token_specification:
                match = pattern.match(code, pos)
                if match:
                    text = match.group(0)
                    if name == 'COMMENT':  # Ignore comments
                        break
                    elif name != 'WHITESPACE':  # Ignore whitespace
                        tokens.append((name, text))
                    pos = match.end()
                    break
            else:
                raise RuntimeError(f"Unexpected character at position {pos}: {code[pos]}")
        return tokens

class ParserNepali:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.current_token = self.tokens[self.current_index] if self.tokens else None
        self.symbol_table = {}

    def advance(self):
        """Move to the next token."""
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None

    def match(self, expected_type):
        """Match the current token with the expected type."""
        if self.current_token and self.current_token[0] == expected_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected {expected_type}, got {self.current_token}")

    def parse(self):
        """Start the parsing process."""
        while self.current_token:
            self.parse_statement()

    def parse_statement(self):
        """Parse a single statement."""
        if self.current_token[0] == 'TYPE':
            self.parse_assignment()
        elif self.current_token[0] == 'PRINT':
            self.parse_print()
        elif self.current_token[0] == 'IF':
            self.parse_if()
        elif self.current_token[0] == 'IDENTIFIER':
            self.parse_assignment()
        else:
            raise SyntaxError(f"Unexpected statement: {self.current_token}")

    def parse_assignment(self):
        """Parse an assignment or variable declaration."""
        var_type = None
        if self.current_token[0] == 'TYPE':
            var_type = self.current_token[1]
            self.advance()

        var_name = self.current_token[1]
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        value = self.parse_expression()
        self.symbol_table[var_name] = value
        self.match('SEMICOLON')

    def parse_expression(self):
        """Parse an expression."""
        left = self.parse_operand()

        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO'):
            operator = self.current_token[0]
            self.advance()
            right = self.parse_operand()
            if operator == 'PLUS':
                left += right
            elif operator == 'MINUS':
                left -= right
            elif operator == 'MULTIPLY':
                left *= right
            elif operator == 'DIVIDE':
                left //= right
            elif operator == 'MODULO':
                left %= right

        return left

    def parse_operand(self):
        """Parse an operand (e.g., a variable or a number)."""
        if self.current_token[0] == 'NUMBER':
            value = int(self.current_token[1])
            self.advance()
            return value
        elif self.current_token[0] == 'IDENTIFIER':
            var_name = self.current_token[1]
            if var_name not in self.symbol_table:
                raise NameError(f"Variable '{var_name}' is not defined.")
            self.advance()
            return self.symbol_table[var_name]
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def parse_condition(self):
        """Parse a condition."""
        left = self.parse_operand()
        operator = self.current_token[0]
        self.advance()
        right = self.parse_operand()

        if operator == 'LT':
            return left < right
        elif operator == 'GT':
            return left > right
        elif operator == 'LE':
            return left <= right
        elif operator == 'GE':
            return left >= right
        elif operator == 'EQ':
            return left == right
        elif operator == 'NEQ':
            return left != right
        else:
            raise SyntaxError(f"Unexpected operator: {operator}")

    def parse_if(self):
        """Parse an IF statement."""
        self.match('IF')
        self.match('LPAREN')
        condition = self.parse_condition()
        self.match('RPAREN')

        if condition:
            self.parse_block()
            if self.current_token and self.current_token[0] == 'ELSE':
                self.advance()
                if self.current_token and self.current_token[0] == 'IF':
                    self.parse_if()  # Handle "Yo Athawa"
                else:
                    self.skip_block()
        else:
            self.skip_block()
            if self.current_token and self.current_token[0] == 'ELSE':
                self.advance()
                if self.current_token and self.current_token[0] == 'IF':
                    self.parse_if()  # Handle "Yo Athawa"
                else:
                    self.parse_block()

    def parse_block(self):
        """Parse a block of statements enclosed in '{' and '}'."""
        self.match('LBRACE')
        while self.current_token and self.current_token[0] != 'RBRACE':
            self.parse_statement()
        self.match('RBRACE')

    def skip_block(self):
        """Skip over a block enclosed in '{' and '}'."""
        self.match('LBRACE')
        brace_count = 1
        while brace_count > 0:
            if self.current_token[0] == 'LBRACE':
                brace_count += 1
            elif self.current_token[0] == 'RBRACE':
                brace_count -= 1
            self.advance()

    def parse_print(self):
        """Parse a PRINT statement."""
        self.match('PRINT')
        self.match('LPAREN')
        value = self.parse_expression()
        self.match('RPAREN')
        self.match('SEMICOLON')
        print(value)
