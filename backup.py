import re

# -----------------------------------------------------------------------------
# Combined Token Definitions for Nepali Language
# -----------------------------------------------------------------------------
# IMPORTANT: The order matters. Comments and whitespace are defined first
# so that they are skipped.
TOKENS_NEPALI = [
    # Comments and whitespace (ignored)
    ('COMMENT', r'//[^\n]*'),
    ('WHITESPACE', r'\s+'),

    # Multi-character relational operators
    ('LE', r'<='),       # less-than-or-equal
    ('GE', r'>='),
    ('NEQ', r'!='),      # not equal
    ('EQ', r'=='),

    # Keywords and control flow constructs
    ('IF', r'Yedi'),
    ('ELSE', r'Athawa'),
    # (For an else-if chain, after Athawa, if the next token is IF [Yedi] the parser will
    # call parse_if() recursively.)
    ('WHILE', r'Jabasamma'),
    ('FOR', r'Kolagi'),
    ('DO', r'Karo'),
    ('RETURN', r'Farkau'),
    ('FUNCTION', r'Karyakram'),

    # I/O keywords
    ('PRINT', r'Dekhau'),
    ('INPUT', r'Linuhoos'),

    # Boolean literals and logical operators
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

    # Data Types (for variable declarations)
    ('TYPE', r'(anka|Dashanka|Shabda|Akshar|Satya|Suchi|Shabdakosh|Khali|Ganna|Sanrachana)'),

    # Symbols and punctuation
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('ASSIGN', r'='),

    # Operators (arithmetic)
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('MODULO', r'%'),

    # Single-character relational operators
    ('LT', r'<'),
    ('GT', r'>'),

    # Literals
    ('NUMBER', r'\d+'),
    ('STRING_LITERAL', r'\".*?\"'),

    # Identifiers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),

    # Catch-all for unknown tokens
    ('UNKNOWN', r'.'),
]

# -----------------------------------------------------------------------------
# LexerNepali: Converts Nepali source code into a stream of tokens.
# -----------------------------------------------------------------------------
class LexerNepali:
    def __init__(self, token_definitions):
        regex_parts = []
        for name, regex in token_definitions:
            regex_parts.append(f"(?P<{name}>{regex})")
        self.regex = re.compile("|".join(regex_parts))
    
    def tokenize(self, code):
        tokens = []
        for mo in self.regex.finditer(code):
            kind = mo.lastgroup
            value = mo.group()
            if kind in ('WHITESPACE', 'COMMENT'):
                continue
            if kind == 'NUMBER':
                value = int(value)
            tokens.append((kind, value))
        return tokens

# -----------------------------------------------------------------------------
# ParserNepali (Interpreter): Implements full language features.
# -----------------------------------------------------------------------------
class ParserNepali:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index] if self.tokens else None
        self.symbol_table = {}  # Global symbol table for variables

    def update_current(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def advance(self):
        self.index += 1
        self.update_current()

    def match(self, expected_type):
        if self.current_token and self.current_token[0] == expected_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected token {expected_type} but got {self.current_token}")

    def parse(self):
        while self.current_token is not None:
            self.parse_statement()

    def parse_statement(self):
        token_type = self.current_token[0]
        if token_type == 'TYPE':  # Variable declaration (e.g. "anka a = 10;")
            self.parse_declaration()
            self.match('SEMICOLON')
        elif token_type == 'IDENTIFIER':  # Assignment statement
            self.parse_assignment()
            self.match('SEMICOLON')
        elif token_type == 'IF':  # Conditional statement (Yedi ... Athawa ...)
            self.parse_if()
        elif token_type == 'FOR':  # For-loop (Kolagi ...)
            self.parse_for()
        elif token_type == 'WHILE':  # While-loop (Jabasamma ...)
            self.parse_while()
        elif token_type == 'DO':  # Do-while loop (Karo { ... } Jabasamma (...); )
            self.parse_do_while()
        elif token_type == 'PRINT':  # Print statement (Dekhau(...);)
            self.parse_print()
            self.match('SEMICOLON')
        else:
            raise SyntaxError(f"Unexpected token in statement: {self.current_token}")

    # --- Declarations and Assignments ---
    def parse_declaration(self):
        # Declaration begins with a TYPE token (e.g. "anka")
        if self.current_token[0] == 'TYPE':
            self.advance()
        else:
            raise SyntaxError("Declaration must begin with a type keyword")
        if self.current_token[0] != 'IDENTIFIER':
            raise SyntaxError("Expected an identifier after type declaration")
        var_name = self.current_token[1]
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        expr = self.parse_expression()
        value = self.evaluate_expression(expr)
        self.symbol_table[var_name] = value

    def parse_assignment(self):
        # Assignment: identifier = expression;
        var_name = self.current_token[1]
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        expr = self.parse_expression()
        value = self.evaluate_expression(expr)
        self.symbol_table[var_name] = value

    # --- Expression Parsing (Arithmetic Expressions) ---
    def parse_expression(self):
        return self.parse_additive()

    def parse_additive(self):
        node = self.parse_term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token[0]
            self.advance()
            right = self.parse_term()
            node = (op, node, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token and self.current_token[0] in ('MULTIPLY', 'DIVIDE', 'MODULO'):
            op = self.current_token[0]
            self.advance()
            right = self.parse_factor()
            node = (op, node, right)
        return node

    def parse_factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.advance()
            return token[1]
        elif token[0] == 'IDENTIFIER':
            self.advance()
            return token[1]
        elif token[0] == 'LPAREN':
            self.match('LPAREN')
            expr = self.parse_expression()
            self.match('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token in expression: {token}")

    def evaluate_expression(self, expr):
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, str):
            if expr in self.symbol_table:
                return self.symbol_table[expr]
            else:
                raise NameError(f"Undefined variable: {expr}")
        elif isinstance(expr, tuple):
            op, left, right = expr
            left_val = self.evaluate_expression(left)
            right_val = self.evaluate_expression(right)
            if op == 'PLUS':
                return left_val + right_val
            elif op == 'MINUS':
                return left_val - right_val
            elif op == 'MULTIPLY':
                return left_val * right_val
            elif op == 'DIVIDE':
                return left_val // right_val  # integer division
            elif op == 'MODULO':
                return left_val % right_val
            else:
                raise ValueError(f"Unknown operator in expression: {op}")
        else:
            raise ValueError(f"Invalid expression: {expr}")

    # --- Condition Parsing ---
    def parse_condition(self):
        # A condition: expression relational_operator expression
        left = self.parse_expression()
        if self.current_token is None:
            raise SyntaxError("Incomplete condition: missing relational operator")
        op_token = self.current_token[0]
        if op_token not in ('LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'):
            raise SyntaxError(f"Expected a relational operator but got {self.current_token}")
        self.advance()
        right = self.parse_expression()
        return (op_token, left, right)

    def evaluate_condition(self, condition):
        op, left_expr, right_expr = condition
        left_val = self.evaluate_expression(left_expr)
        right_val = self.evaluate_expression(right_expr)
        if op == 'LT':
            return left_val < right_val
        elif op == 'LE':
            return left_val <= right_val
        elif op == 'GT':
            return left_val > right_val
        elif op == 'GE':
            return left_val >= right_val
        elif op == 'EQ':
            return left_val == right_val
        elif op == 'NEQ':
            return left_val != right_val
        else:
            raise ValueError(f"Unknown condition operator: {op}")

    # --- Print Statement ---
    def parse_print(self):
        # PRINT is Dekhau
        if self.current_token[0] in ('PRINT',):
            self.advance()
        else:
            raise SyntaxError("Expected print keyword")
        self.match('LPAREN')
        expr = self.parse_expression()
        value = self.evaluate_expression(expr)
        print(value)
        self.match('RPAREN')

    # --- IF Statement (Yedi ... Athawa ...) with support for else-if ---
    def parse_if(self):
        self.match('IF')  # Yedi
        self.match('LPAREN')
        condition = self.parse_condition()
        self.match('RPAREN')
        if self.evaluate_condition(condition):
            self.parse_block()
            # If an ELSE clause follows, skip it.
            if self.current_token and self.current_token[0] == 'ELSE':
                self.advance()
                # Check for else-if (Yedi) after Athawa
                if self.current_token and self.current_token[0] == 'IF':
                    self.parse_if()
                else:
                    self.skip_block()
        else:
            self.skip_block()
            if self.current_token and self.current_token[0] == 'ELSE':
                self.advance()
                if self.current_token and self.current_token[0] == 'IF':
                    self.parse_if()
                else:
                    self.parse_block()

    def parse_block(self):
        self.match('LBRACE')
        while self.current_token and self.current_token[0] != 'RBRACE':
            self.parse_statement()
        self.match('RBRACE')

    def skip_block(self):
        _ = self.capture_block_tokens()

    # --- FOR Loop (Kolagi (init; condition; increment) { block } ) ---
    def parse_for(self):
        self.match('FOR')  # Kolagi
        self.match('LPAREN')
        # Initialization: either a declaration or an assignment.
        if self.current_token[0] == 'TYPE':
            self.parse_declaration()
        elif self.current_token[0] == 'IDENTIFIER':
            self.parse_assignment()
        else:
            raise SyntaxError("Invalid initialization in for-loop")
        self.match('SEMICOLON')
        condition = self.parse_condition()
        self.match('SEMICOLON')
        increment = self.parse_increment()
        self.match('RPAREN')
        body_tokens = self.capture_block_tokens()
        while self.evaluate_condition(condition):
            body_parser = ParserNepali(body_tokens.copy())
            body_parser.symbol_table = self.symbol_table
            body_parser.parse()
            self.execute_increment(increment)

    def parse_increment(self):
        var_name = self.current_token[1]
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        expr = self.parse_expression()
        return (var_name, expr)

    def execute_increment(self, increment):
        var_name, expr = increment
        value = self.evaluate_expression(expr)
        self.symbol_table[var_name] = value

    # --- WHILE Loop (Jabasamma (condition) { block } ) ---
    def parse_while(self):
        self.match('WHILE')  # Jabasamma
        self.match('LPAREN')
        condition = self.parse_condition()
        self.match('RPAREN')
        body_tokens = self.capture_block_tokens()
        while self.evaluate_condition(condition):
            body_parser = ParserNepali(body_tokens.copy())
            body_parser.symbol_table = self.symbol_table
            body_parser.parse()

    # --- DO-WHILE Loop (Karo { block } Jabasamma (condition); ) ---
    def parse_do_while(self):
        self.match('DO')  # Karo
        body_tokens = self.capture_block_tokens()
        self.match('WHILE')  # Jabasamma
        self.match('LPAREN')
        condition = self.parse_condition()
        self.match('RPAREN')
        self.match('SEMICOLON')
        while True:
            body_parser = ParserNepali(body_tokens.copy())
            body_parser.symbol_table = self.symbol_table
            body_parser.parse()
            if not self.evaluate_condition(condition):
                break

    # --- Utility: Capture Block Tokens ---
    def capture_block_tokens(self):
        if self.current_token[0] != 'LBRACE':
            raise SyntaxError("Expected '{' at start of block")
        start_index = self.index
        brace_count = 0
        while self.index < len(self.tokens):
            token_type = self.tokens[self.index][0]
            if token_type == 'LBRACE':
                brace_count += 1
            elif token_type == 'RBRACE':
                brace_count -= 1
                if brace_count == 0:
                    block_tokens = self.tokens[start_index + 1 : self.index]
                    self.index += 1  # consume the closing RBRACE
                    self.update_current()
                    return block_tokens
            self.index += 1
        raise SyntaxError("Missing closing '}' for block")

# -----------------------------------------------------------------------------
# Main: Example Usage
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    source_code = r'''
        // Nepali Language Test Code

        // Variable declarations and assignments:
        anka a = 10;
        anka b = 5;
        
        // Arithmetic expressions:
        anka c = a + b;
        Dekhau(c);     // Expected output: 15
        
        anka d = c - b;
        Dekhau(d);     // Expected output: 10
        
        anka e = d * b;
        Dekhau(e);     // Expected output: 50
        
        anka f = e / b;
        Dekhau(f);     // Expected output: 10   (integer division)
        
        anka g = e % b;
        Dekhau(g);     // Expected output: 0
        
        // IF statement with else-if:
        anka x = 20;
        anka y = 30;
        Yedi (x > y) {
            Dekhau(100);
        } Athawa Yedi (x > 10) {
            Dekhau(10);
        } Athawa {
            Dekhau(0);
        }
        
        // FOR loop:
        Kolagi ( anka i = 0; i < 3; i = i + 1 ) {
            Dekhau(i);
        }
        
        // WHILE loop:
        Jabasamma ( a < 15 ) {
            a = a + 1;
            Dekhau(a);
        }
        
        // DO-WHILE loop:
        Karo {
            b = b - 1;
            Dekhau(b);
        } Jabasamma ( b > 0 );
        
        anka x = 10;
        anka y = 5;
        Yedi (x > y) {
            Dekhau(x);
        } Athawa {
            Dekhau(y);
        }
    '''
    
    lexer = LexerNepali(TOKENS_NEPALI)
    tokens = lexer.tokenize(source_code)
    parser = ParserNepali(tokens)
    parser.parse()
