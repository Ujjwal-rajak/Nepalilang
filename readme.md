# 🇳🇵 Nepalilang - नेपालीमा प्रोग्रामिङ

**Nepalilang** is a Python-based programming language that uses **Nepali-style syntax**, developed by **Ujjwal Kumar Rajak** and **Jigmi Bhutia**. It is designed to make programming more accessible for Nepali-speaking learners by introducing core programming concepts in their native language.

---

## 🎥 Demo Video

🎬 Watch the demo:

![Nepalilang Demo](./nepalilang.mp4)
---


---

## ✨ Key Features

- ✅ **Nepali Syntax**: Write code using native Nepali keywords
- ➕ **Arithmetic Operations**: `+`, `-`, `*`, `/`, `%`
- 📦 **Variables**: Declare using `anka`
- 🖨️ **Output**: Display results using `dekhau`
- 🔁 **Loops**:
  - `laagi` — For loop
  - `samma` — While loop
  - `gara ... samma` — Do-while loop
- 🔀 **Conditionals**:
  - `yadi` — If
  - `natra` — Else

---

## ⚙️ Installation

Install Nepalilang using pip:

```bash
pip install nepalilang
📝 Basic Usage
python
Copy
Edit
import nepalilang

if __name__ == "__main__":
    code = r'''
    anka a = 10;
    anka b = 5;
    anka c = a + b;
    dekhau(c);   # Output: 15

    anka i = 0;
    laagi (anka i = 0; i < 3; i = i + 1) {
        dekhau(i);
    }

    anka j = 0;
    gara {
        dekhau(j);
        j = j + 1;
    } samma (j <= 3);

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
🔄 Loop Examples
🔁 For Loop
text
Copy
Edit
laagi (anka i = 0; i < 3; i = i + 1) {
    dekhau(i);
}
🔁 Do-While Loop
text
Copy
Edit
anka j = 0;
gara {
    dekhau(j);
    j = j + 1;
} samma (j <= 3);

🙋‍♂️ Why Nepalilang?
🌐 Breaks the language barrier for native Nepali speakers

🚀 Helps beginners transition into English-based programming

🏫 Ideal for educational use in schools and coding workshops

🧱 Covers all fundamental programming concepts

🤝 Contributing
We welcome contributions! Whether it's improving documentation, adding new features, or reporting bugs—your input helps make Nepalilang better.

This project was developed by :

[Ujjwal Kumar Rajak (LinkedIn)](https://www.linkedin.com/in/ujjwal-kumar-rajak/)
[Jigmi Bhutia (LinkedIn)](https://www.linkedin.com/in/jigmi-dorjee-bhutia-1414aa321/)

Feel free to fork the repository and submit pull requests or issues.

📜 License
MIT License – Free for educational and personal use.
See the LICENSE file for more details.
