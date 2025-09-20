import json, time, pathlib

def save_json(data, out="results/report.json"):
    outp = pathlib.Path(out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    data["generated_at"] = int(time.time())
    outp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(outp)

def save_dashboard(data, html="docs/index.html"):
    p = pathlib.Path(html)
    p.parent.mkdir(parents=True, exist_ok=True)
    tpl = p.read_text(encoding="utf-8")
    tpl = tpl.replace("/*__DATA__*/", "window.TGSEC_DATA = " + json.dumps(data, ensure_ascii=False) + ";")
    p.write_text(tpl, encoding="utf-8")
    return str(p)
