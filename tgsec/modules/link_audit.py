import re

URL_RX = re.compile(r"https?://([A-Za-z0-9\.\-]+)(/[^\s]*)?")

SUSPICIOUS = [
    "te1egram", "telegraam", "telergram", "telegrarn", "telegram-login",
    "gift-telegram", "verify-telegram", "bonus-telegram"
]

def audit_text(text: str):
    risky = []
    for m in URL_RX.finditer(text):
        domain = m.group(1).lower()
        if any(bad in domain for bad in SUSPICIOUS):
            risky.append(domain)
    return sorted(set(risky))
