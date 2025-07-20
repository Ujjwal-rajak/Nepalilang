Nepalilang

Nepalilang is a simple programming language developed by Ujjwal Kumar Rajak and Jigmi Bhutia during their internship at Beasova. It supports basic arithmetic operations, loops, and conditional statements, providing an easy-to-use syntax inspired by the Nepali language.

Features
Supports arithmetic operations (+, -, *, /, %).
Supports variable declaration using anka.
Printing is done using dekhau.
Supports loops (for, while, do while) and conditional statements (if-else).


Installation
To install Nepalilang, use:

pip install nepalilang

Below is an example demonstrating basic arithmetic operations and control structures in Nepalilang:


    import nepalilang  

    if __name__ == "__main__":  
        code = r'''  

        anka a = 10;  
        anka b = 5;  
        anka c = a + b;  
        dekhau(c);  

        anka i = 0;  
        laagi (anka i = 0; i < 3; i = i + 1) {  
            dekhau(i);  
        }  

        anka j = 0;  
        gara {  
            dekhau(j);  
            j = j + 1;  
        }  
        samma (j <= 3);  

        anka k = 3;  
        samma (k > 0) {  
            dekhau(k);  
            k = k - 1;  
        }  

        anka a = 10;  
        yadi (a > 5) {  
            dekhau(a);  
        } natra {  
            dekhau(0);  
        }  

        '''  

        nepalilang.run_code(code)  

As part of their work at Beasova, Ujjwal kumar Rajak and Jigmi Bhutia contributed to the development of Nepalilang to make coding more accessible by incorporating Nepali syntax into a programming language.

