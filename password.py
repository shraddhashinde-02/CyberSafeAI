import re

def check_password(password):
    score = 0
    suggestions = []

    # Minimum length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number.")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one special character.")

    # Result
    if score == 5:
        strength = "🟢 Strong Password"
    elif score >= 3:
        strength = "🟡 Medium Password"
    else:
        strength = "🔴 Weak Password"

    result = f"Password Strength: {strength}\n\n"

    if suggestions:
        result += "Suggestions:\n"
        for item in suggestions:
            result += item + "\n"

    return result