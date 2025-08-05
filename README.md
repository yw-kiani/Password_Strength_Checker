## 🔒 Password Strength Analyzer

A simple yet powerful Python script to **analyze the strength of user-entered passwords** based on multiple criteria such as length, complexity, and whether it appears in a list of weak/common passwords.

---

### 🧩 Features

* ✅ Detects **uppercase**, **lowercase**, **numbers**, and **special characters**
* ❌ Flags **commonly used passwords**
* 📏 Evaluates password **length**
* 📊 Gives a clear **strength rating**: Weak ❌, Moderate ⚠️, or Strong 💪
* 🧠 Provides **specific suggestions** to improve password quality

---

### 🛠️ How to Use

1. Clone or download this repository.
2. Run the Python file:

```bash
python password_checker.py
```

3. Type a password when prompted.
4. Receive instant feedback and a strength rating.

---

### 📌 Example

```
Type your password: Hello123!

Strength: Strong 💪
Suggestions:
- ✅ Has uppercase letter.
- ✅ Has lowercase letter.
- ✅ Has digit.
- ✅ Has special character.
- ✅ Good length.
```

---

### 🔐 Weak Password Dictionary

This tool checks if your password is among a list of very common (and insecure) passwords, like:

```python
weak_pass_list = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "password1", "1234", "admin", "password123"
]
```

📥 **Tip:** You can expand this list by searching online for files like `rockyou.txt` or `top-1000-passwords.txt`.

---

### 🤖 Password Scoring Logic

| Criteria                   | Points           |
| -------------------------- | ---------------- |
| Contains uppercase letter  | +1               |
| Contains lowercase letter  | +1               |
| Contains digit             | +1               |
| Contains special character | +1               |
| Length ≥ 8 characters      | +1               |
| Found in weak list         | Score reset to 0 |

---

### 📄 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

---

### 🙋 Contribute

Feel free to fork the repo and contribute improvements, new features, or larger password dictionaries.

---
