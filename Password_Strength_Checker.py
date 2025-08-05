import re

# Weak password dictionary
weak_pass_list = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "123123", "password1", "1234", "admin", "password123"
]

def analyze_password_strength(pwd):
    points = 0
    comments = []

    # Check for uppercase characters
    if re.search(r"[A-Z]", pwd):
        points += 1
        comments.append("✅ Has uppercase letter.")
    else:
        comments.append("⚠️ Add an uppercase letter.")

    # Check for lowercase characters
    if re.search(r"[a-z]", pwd):
        points += 1
        comments.append("✅ Has lowercase letter.")
    else:
        comments.append("⚠️ Add a lowercase letter.")

    # Check for digits
    if re.search(r"\d", pwd):
        points += 1
        comments.append("✅ Has digit.")
    else:
        comments.append("⚠️ Add a number.")

    # Check for symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        points += 1
        comments.append("✅ Has special character.")
    else:
        comments.append("⚠️ Add a special character.")

    # Check for common passwords
    if pwd.lower() in weak_pass_list:
        comments.append("❌ This is a very common password.")
        points = 0  # Immediately make score 0
    else:
        pass  # No comment needed

    # Check password length
    if len(pwd) < 6:
        comments.append("❌ Too short. Use at least 6 characters.")
    elif len(pwd) >= 8:
        points += 1
        comments.append("✅ Good length.")
    else:
        comments.append("⚠️ Use 8 or more characters.")

    # Determine result
    final_verdict = ""
    if points == 5:
        final_verdict = "Strong 💪"
    elif 3 <= points < 5:
        final_verdict = "Moderate ⚠️"
    else:
        final_verdict = "Weak ❌"

    return final_verdict, comments

# Execution block
if __name__ == "__main__":
    user_input = input("Type your password: ")
    result, suggestions = analyze_password_strength(user_input)
    print(f"\nStrength: {result}")
    print("Suggestions:")
    for c in suggestions:
        print(f"- {c}")
