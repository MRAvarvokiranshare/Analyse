import argparse, json, sys, pathlib
from rich.console import Console
from rich.table import Table
from tgsec.colors import SEVERITY as S
from tgsec.modules.scan_secrets import scan_path
from tgsec.modules.link_audit import audit_text
from tgsec.modules.webhook_monitor import check_webhook
from tgsec.report import save_json, save_dashboard

c = Console()

def banner():
    c.print("[bold magenta]┌──────────────────────────────────────────┐[/]")
    c.print("[bold magenta]│[/]  [bold cyan]TG-SEC[/] [white]·[/] [green]Termux/Kali[/] [white]·[/] [yellow]GitHub Actions[/]  [bold magenta]│[/]")
    c.print("[bold magenta]└──────────────────────────────────────────┘[/]")

def cmd_scan(args):
    banner()
    c.print(f"[{S['token']['color']}] {S['token']['emoji']} Scanning secrets in:[/] {args.path}")
    findings = scan_path(args.path)
    table = Table(title="Secrets findings", show_lines=True)
    table.add_column("Type"); table.add_column("File"); table.add_column("Snippet")
    for f in findings:
        table.add_row(f["type"], f["file"], f["snippet"])
    if findings:
        c.print(table)
        c.print(f"[{S['high']['color']}] {S['high']['emoji']} High risk:[/] remove tokens from code, use .env")
    else:
        c.print(f"[{S['ok']['color']}] {S['ok']['emoji']} No secrets found.")
    return {"scan_secrets": findings}

def cmd_links(args):
    banner()
    txt = pathlib.Path(args.file).read_text(encoding="utf-8", errors="ignore")
    risky = audit_text(txt)
    if risky:
        c.print(f"[{S['warn']['color']}] {S['warn']['emoji']} Suspicious domains found:")
        for d in risky:
            c.print(f"   [{S['link']['color']}] {S['link']['emoji']} {d}")
    else:
        c.print(f"[{S['ok']['color']}] {S['ok']['emoji']} No suspicious links.")
    return {"risky_links": risky}

def cmd_webhook(args):
    banner()
    results = []
    for url in args.urls:
        r = check_webhook(url, args.secret_preview)
        color = S['ok']['color'] if r.get("ok") else S['high']['color']
        emoji = S['ok']['emoji'] if r.get("ok") else S['high']['emoji']
        c.print(f"[{color}] {emoji} {url} → {r.get('status')} ({r.get('latency_ms')} ms)")
        results.append(r)
    return {"webhooks": results}

def main():
    p = argparse.ArgumentParser(prog="tgsec", description="Telegram security helper (Termux/Kali + GitHub)")
    sub = p.add_subparsers(dest="cmd")

    s1 = sub.add_parser("scan-secrets"); s1.add_argument("--path", required=True)
    s2 = sub.add_parser("links"); s2.add_argument("--file", required=True)
    s3 = sub.add_parser("webhook"); s3.add_argument("--secret-preview", default=""); s3.add_argument("urls", nargs="+")

    s1.add_argument("--out-json", default="results/report.json")
    s2.add_argument("--out-json", default="results/report.json")
    s3.add_argument("--out-json", default="results/report.json")
    for sp in (s1, s2, s3):
        sp.add_argument("--dashboard", action="store_true")

    args = p.parse_args()
    if not args.cmd:
        p.print_help(); sys.exit(0)

    if args.cmd == "scan-secrets":
        data = cmd_scan(args)
    elif args.cmd == "links":
        data = cmd_links(args)
    else:
        data = cmd_webhook(args)

    path = save_json(data, args.out_json)
    c.print(f"[{S['info']['color']}] {S['info']['emoji']} Saved JSON → {path}")

    if args.dashboard:
        save_dashboard(data)
        c.print(f"[{S['audit']['color']}] {S['audit']['emoji']} Dashboard updated → docs/index.html")

if __name__ == "__main__":
    main()
