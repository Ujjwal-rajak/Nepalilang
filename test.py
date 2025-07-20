# Importing necessary classes from the Nepali lexer and parser
from nepalilang import LexerNepali, ParserNepali, TOKENS_NEPALI

# Example Nepali-like code to parse
code = """
anka x = 10;
anka y = 5;
Dekhau(x);
Dekhau(y);
x = x + y;
Dekhau(x);
"""

# Step 1: Lexical Analysis (Tokenization)
lexer = LexerNepali(TOKENS_NEPALI)
tokens = lexer.tokenize(code)
print("Tokens:", tokens)

# Step 2: Parsing the tokens
parser = ParserNepali(tokens)
parser.parse()
