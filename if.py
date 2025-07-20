from nepalilang import LexerNepali, ParserNepali, TOKENS_NEPALI
if __name__ == "__main__":
    code = """
    anka x = 10;
    anka y = 5;
    Yedi (x > y) {
        Dekhau(x);
    } Athawa {
        Dekhau(y);
    }
    """
    lexer = LexerNepali(TOKENS_NEPALI)
    tokens = lexer.tokenize(code)
    parser = ParserNepali(tokens)
    parser.parse()
