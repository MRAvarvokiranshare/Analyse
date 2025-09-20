import time, requests
from urllib.parse import urlparse

def check_webhook(url: str, secret_preview: str = ""):
    t0 = time.time()
    headers = {}
    if secret_preview:
        headers["X-Telegram-Bot-Api-Secret-Token"] = secret_preview
    try:
        r = requests.get(url, headers=headers, timeout=7)
        latency = int((time.time() - t0) * 1000)
        return {
            "url": url, "status": r.status_code, "ok": r.ok,
            "latency_ms": latency, "tls": urlparse(url).scheme == "https"
        }
    except requests.RequestException as e:
        return {"url": url, "status": None, "ok": False, "latency_ms": None, "error": str(e)}
