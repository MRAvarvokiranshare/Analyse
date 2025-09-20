import re, pathlib

PATTERNS = {
    "telegram_bot_token": re.compile(r"\b(\d{5,}:[A-Za-z0-9_-]{20,})\b"),
    "tg_api_id": re.compile(r"\bapi_id\s*=\s*(\d{5,})\b", re.IGNORECASE),
    "tg_api_hash": re.compile(r"\bapi_hash\s*=\s*['\"][0-9a-f]{32}['\"]\b", re.IGNORECASE),
    "jwt": re.compile(r"\beyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "aws_secret": re.compile(r"\b[A-Za-z0-9/+=]{40}\b"),
}

def scan_path(path: str, max_size=2_000_000):
    root = pathlib.Path(path)
    findings = []
    for p in root.rglob("*"):
        if p.is_file() and p.stat().st_size <= max_size:
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for name, rx in PATTERNS.items():
                for m in rx.finditer(content):
                    findings.append({
                        "type": name,
                        "file": str(p.relative_to(root)),
                        "snippet": m.group(0)[:6] + "...",
                    })
    return findings
