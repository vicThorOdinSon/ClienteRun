import re

def normalize_run(run: str) -> str:
    if not run:
        return ""
    s = str(run).strip().upper().replace(".", "").replace(" ", "")
    s = s.replace("—", "-").replace("–", "-")
    if "-" not in s and len(s) >= 2:
        s = s[:-1] + "-" + s[-1]
    return s

def highlight(text, color="#FFD700"):
    return f"<span style='background-color:{color};padding:2px 6px;border-radius:4px'>{text}</span>"
