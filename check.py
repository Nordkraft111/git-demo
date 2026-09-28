#!/usr/bin/env python3
"""Small dependency-free check for the portfolio and the exercise's real history."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import subprocess

ROOT = Path(__file__).resolve().parent


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True)


html = (ROOT / "index.html").read_text()
doc = Document(html)
require(html.lstrip().lower().startswith("<!doctype html>"), "HTML5 doctype mangler")
require(any(t == "html" and a.get("lang") == "da" for t, a in doc.elements), "Dansk sprog mangler")
require(sum(t == "h1" for t, _ in doc.elements) == 1, "Der skal være præcis én h1")
require(sum(t == "main" for t, _ in doc.elements) == 1, "Der skal være præcis ét main-element")
ids = [a["id"] for _, a in doc.elements if "id" in a]
require(len(ids) == len(set(ids)), "Et id er brugt flere gange")
last_heading = 0
for tag, attrs in doc.elements:
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        require(level <= last_heading + 1, "Overskriftshierarkiet springer et niveau over")
        last_heading = level
    if "href" in attrs:
        link = urlsplit(attrs["href"])
        if not link.scheme and not link.netloc:
            require(not link.path or (ROOT / link.path).is_file(), "Manglende lokal fil: " + link.path)
            if link.fragment and link.path in ("", "index.html"):
                require(link.fragment in ids, "Manglende anker: " + link.fragment)
    require(tag not in ("script", "form", "iframe"), "Øvelsen skal være statisk uden dataindsamling")
require(any(t == "meta" and a.get("name") == "viewport" for t, a in doc.elements), "Viewport mangler")
require(any(t == "a" and a.get("href") == "#indhold" for t, a in doc.elements), "Skip-link mangler")
require(".idea/" in (ROOT / ".gitignore").read_text().splitlines(), ".idea/ er ikke ignoreret")
for filename in ("styles.css", "README.md", "PROMPT.md"):
    require((ROOT / filename).stat().st_size > 0, filename + " mangler eller er tom")
print("PASS: lokale filer, links, sprog, overskrifter, skip-link og .gitignore")

if (ROOT / ".git").exists():
    revisions = git("rev-list", "--reverse", "HEAD").splitlines()
    require(len(revisions) >= 2, "De første to øvelsescommits mangler")
    first, second = revisions[:2]
    require(git("log", "-1", "--format=%s", first).strip() == "Første version", "Første commit-besked afviger")
    require(git("log", "-1", "--format=%s", second).strip() == "Tilføjet velkomsttekst", "Anden commit-besked afviger")
    first_html = git("show", first + ":index.html")
    second_html = git("show", second + ":index.html")
    require("<h1>Mit første Git-projekt</h1>" in first_html, "Første version har forkert h1")
    require("<h1>Velkommen til mit Git-projekt</h1>" in second_html, "Anden version har forkert h1")
    require(second_html.count("<p>") == first_html.count("<p>") + 1, "Anden version skal tilføje ét tekstafsnit")
    ignored = git("check-ignore", "--no-index", ".idea/workspace.xml").strip()
    require(ignored == ".idea/workspace.xml", ".idea-reglen virker ikke")
    print("PASS: reelle snapshots, commit-beskeder og ignorerede PhpStorm-indstillinger")
else:
    print("INFO: ZIP-udgave uden .git; historikkontrol springes over")
