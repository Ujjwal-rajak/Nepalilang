# Nepalilang - नेपालीमा प्रोग्रामिङ
Nepalilang is a Python-based programming language that uses Nepali-style syntax. It was developed by Ujjwal Kumar Rajak and Jigmi Bhutia with the goal of making programming more accessible for Nepali-speaking learners by introducing core programming concepts in their native language.

🎥 Demo Video
🎬 A demo video is available in the repository! You can find it named nepalilang.mp4 within this project's files.


✨ Key Features
Nepali Syntax: Write code using native Nepali keywords.

Arithmetic Operations: Supports +, -, *, /, %.

Variables: Declare variables using anka.

Output: Display results using dekhau.

Loops:

laagi — For loop

samma — While loop

gara ... samma — Do-while loop

Conditionals:

yadi — If

natra — Else

⚙️ Installation
Install Nepalilang using pip:

Bash

pip install nepalilang
📝 Basic Usage
Here's a basic example of how to use Nepalilang:

Python

import nepalilang

if __name__ == "__main__":
    code = r'''
    anka a = 10;
    anka b = 5;
    anka c = a + b;
    dekhau(c);   # Output: 15

    anka i = 0;
    laagi (anka i = 0; i < 3; i = i + 1) {
        dekhau(i); # Outputs: 0, 1, 2
    }

    anka j = 0;
    gara {
        dekhau(j);
        j = j + 1;
    } samma (j <= 3); # Outputs: 0, 1, 2, 3

    anka k = 3;
    samma (k > 0) {
        dekhau(k);
        k = k - 1;
    } # Outputs: 3, 2, 1

    anka a = 10;
    yadi (a > 5) {
        dekhau(a); # Outputs: 10
    } natra {
        dekhau(0);
    }
    '''
    nepalilang.run_code(code)
🔄 Loop Examples
For Loop
Plaintext

laagi (anka i = 0; i < 3; i = i + 1) {
    dekhau(i);
}
Do-While Loop
Plaintext

anka j = 0;
gara {
    dekhau(j);
    j = j + 1;
} samma (j <= 3);
🙋‍♂️ Why Nepalilang?
Breaks the Language Barrier: Makes programming more accessible for native Nepali speakers.

Smooth Transition: Helps beginners transition into English-based programming concepts.

Educational Tool: Ideal for use in schools and coding workshops.

Foundational: Covers all fundamental programming concepts.

🤝 Contributing
We welcome contributions! Whether you're improving documentation, adding new features, or reporting bugs—your input helps make Nepalilang better.

This project was developed by:

Ujjwal Kumar Rajak (Lead Developer)

LinkedIn Profile: https://www.linkedin.com/in/ujjwal-kumar-rajak/

Jigmi Bhutia (Co-Developer)

LinkedIn Profile: https://www.linkedin.com/in/jigmi-dorjee-bhutia-1414aa321/

Feel free to fork the repository and submit pull requests or issues.

📜 License
Nepalilang is released under the MIT License, making it free for educational and personal use. See the LICENSE file for more details.
