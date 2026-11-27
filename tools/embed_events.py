#!/usr/bin/env python3
"""Copy events.json into index.html so the page still shows events if the fetch fails.
Run from the repo root: python3 tools/embed_events.py"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "events.json").read_text(encoding="utf-8"))
blob = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
page = root / "index.html"
html = page.read_text(encoding="utf-8")
pat = re.compile(r'(<script type="application/json" id="events-embedded">).*?(</script>)', re.S)
if not pat.search(html):
    raise SystemExit("placeholder script#events-embedded not found in index.html")
page.write_text(pat.sub(lambda m: m.group(1) + blob + m.group(2), html, count=1), encoding="utf-8")
print("embedded", len(data.get("events", [])), "events")
