"""Plain-language gate for the Core Course: strips everything that is not running prose, then measures it.

Lessons are written with one paragraph per line (no hard wrapping), so a newline ends a sentence as well as . ! ?"""
import re


def prose(md: str) -> str:
    t = re.sub(r'(?s)\A---\n.*?\n---\n', '', md)          # front matter
    t = re.sub(r'(?s)```.*?```', ' ', t)                  # code blocks
    t = re.sub(r'(?m)^\s*\|.*$', ' ', t)                  # table rows
    t = re.sub(r'(?m)^#+\s.*$', ' ', t)                   # headings
    t = re.sub(r'`[^`]*`', ' thing ', t)                  # inline code counts as one plain word
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)        # links keep their text
    t = re.sub(r'(?m)^\s*(?:[-*+]|\d+[.)])\s+', '', t)    # list markers
    return re.sub(r'[*_>]', '', t)


def _syll(w: str) -> int:
    w = w.lower()
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and not w.endswith(('le', 'ee')) and n > 1:
        n -= 1
    return max(n, 1)


def readability(md: str) -> dict:
    t = prose(md)
    sents = [s for s in re.split(r'(?<=[.!?])\s+|\n+', t) if re.search(r'[A-Za-z]', s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", t)
    if not sents or not words:
        return dict(words=0, sentences=0, avg_words=0.0, flesch=100.0)
    syl = sum(_syll(w) for w in words)
    asl, asw = len(words) / len(sents), syl / len(words)
    return dict(words=len(words), sentences=len(sents), avg_words=round(asl, 1),
                flesch=round(206.835 - 1.015 * asl - 84.6 * asw, 1))
