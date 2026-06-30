import re

def check_url(url):
    suspicious_keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "bank",
        "signin",
        "confirm",
        "password",
        "wallet",
        "gift",
        "free",
        "bonus",
        "win",
        "crypto"
    ]

    score = 0
    reasons = []

    # Check URL length
    if len(url) > 75:
        score += 1
        reasons.append("⚠ URL is unusually long.")

    # Check for IP address
    if re.search(r"https?://(\d{1,3}\.){3}\d{1,3}", url):
        score += 2
        reasons.append("⚠ URL uses an IP address instead of a domain name.")

    # Count hyphens
    if url.count("-") >= 2:
        score += 1
        reasons.append("⚠ URL contains multiple hyphens.")

    # Check suspicious keywords
    url_lower = url.lower()
    for word in suspicious_keywords:
        if word in url_lower:
            score += 1
            reasons.append(f"⚠ Suspicious keyword found: {word}")

    # Final result
    if score >= 4:
        status = "🔴 High Risk - Possible Phishing Website"
    elif score >= 2:
        status = "🟡 Medium Risk - Be Careful"
    else:
        status = "🟢 Low Risk"

    result = f"URL Analysis Result\n\nStatus: {status}\n\n"

    if reasons:
        result += "Reasons:\n"
        for reason in reasons:
            result += reason + "\n"
    else:
        result += "No suspicious indicators were detected."

    return result