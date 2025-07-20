import nepalilang


if __name__ == "__main__":
    code = r"""
    anka a = 10;
    anka b = 5;
    anka c = a + b;
    Dekhau(c);

    anka d = c - b;
    Dekhau(d);

    anka e = d * b;
    Dekhau(e);

    anka f = e / b;
    Dekhau(f);

    anka g = e % b;
    Dekhau(g);
    """
    
    nepalilang.run_code(code)