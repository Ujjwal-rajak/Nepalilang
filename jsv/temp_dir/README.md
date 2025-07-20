Nepalilang

Nepalilang is a simple programming language that supports basic arithmetic operations and loops. It provides an easy-to-use syntax inspired by Nepali keywords for programming.

Features

Supports arithmetic operations (+, -, *, /, %).

Supports variable declaration using ank.

Printing is done using dekhau.

Supports loops (for, while,do while) and conditional statements (if-else).

Installation

To install Nepalilang, use:

pip install nepalilang

Example Usage

Below is an example demonstrating basic arithmetic operations in nepalilang:

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