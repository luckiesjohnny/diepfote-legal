#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt aus src/*.md die ausgelieferten HTML-Seiten.

Die Markdown-Dateien sind die Quelle und stammen aus dem App-Repository
(Verzeichnis legal/). Geaendert wird dort, hierher kopiert, dann `python3 build.py`.

Bewusst ohne Jekyll und ohne fremde Bibliothek: Was GitHub Pages ausliefert, ist genau das,
was hier erzeugt und committet wurde. Ein Rechtstext soll nicht davon abhaengen, ob ein
Build auf fremder Infrastruktur durchlaeuft.
"""
import html
import io
import os
import re

SEITEN = [
    ("datenschutz", "Datenschutzerklärung"),
    ("impressum", "Impressum"),
    ("nutzungsbedingungen", "Nutzungsbedingungen"),
]

RAHMEN = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} – Die Pfote</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav><a href="index.html">Die Pfote</a><span>{navigation}</span></nav>
<main>
{inhalt}
</main>
<footer>Android-App &bdquo;Die Pfote&ldquo; – Tierarztsuche, Notdienst und GOT-Kostenrechner für Hunde</footer>
</body>
</html>
"""


def inline(text):
    """Fettdruck und Inline-Code, nachdem alles HTML-Gefaehrliche entschaerft ist."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def md_to_html(md):
    zeilen = md.split("\n")
    aus, absatz, liste, zitat = [], [], [], []

    def absatz_schliessen():
        if absatz:
            aus.append("<p>" + inline(" ".join(absatz)) + "</p>")
            del absatz[:]

    def liste_schliessen():
        if liste:
            aus.append("<ul>")
            aus.extend("<li>" + inline(" ".join(p)) + "</li>" for p in liste)
            aus.append("</ul>")
            del liste[:]

    def zitat_schliessen():
        if zitat:
            aus.append("<blockquote>" + inline(" ".join(zitat)) + "</blockquote>")
            del zitat[:]

    def alles_schliessen():
        absatz_schliessen(); liste_schliessen(); zitat_schliessen()

    for roh in zeilen:
        zeile = roh.rstrip()
        if not zeile.strip():
            alles_schliessen()
            continue
        ueberschrift = re.match(r"^(#{1,4}) +(.*)$", zeile)
        if ueberschrift:
            alles_schliessen()
            stufe = len(ueberschrift.group(1))
            aus.append("<h%d>%s</h%d>" % (stufe, inline(ueberschrift.group(2)), stufe))
            continue
        if zeile.startswith("- ") or zeile.startswith("* "):
            absatz_schliessen(); zitat_schliessen()
            liste.append([zeile[2:].strip()])
            continue
        if zeile.startswith(">"):
            absatz_schliessen(); liste_schliessen()
            zitat.append(zeile.lstrip(">").strip())
            continue
        if liste and roh.startswith(("  ", "\t")):
            liste[-1].append(zeile.strip())
            continue
        liste_schliessen(); zitat_schliessen()
        absatz.append(zeile.strip())

    alles_schliessen()
    return "\n".join(aus)


VERBOTEN = [
    (re.compile(r"nicht f\u00fcr die Ver\u00f6ffentlichung", re.I), "redaktionelle Anmerkung"),
    (re.compile(r"Hinweis f\u00fcr dich", re.I), "redaktionelle Anmerkung"),
    (re.compile(r"\[[A-Z\u00c4\u00d6\u00dc][A-Z\u00c4\u00d6\u00dc0-9 ./\u00a7-]{3,}\]"), "ungefuellter Platzhalter"),
]


def pruefen(name, md):
    """Bricht ab, bevor etwas veroeffentlicht wird, das niemand lesen soll.

    Der Anlass: Im Impressum stand eine Anmerkung an den Autor, eingeleitet mit "Hinweis fuer
    dich, nicht fuer die Veroeffentlichung" - und stand damit ab dem ersten Build im Netz.
    Solche Notizen gehoeren in die README des App-Repositories, Platzhalter gar nirgendwohin.
    """
    for zeilennr, zeile in enumerate(md.split("\n"), 1):
        for muster, art in VERBOTEN:
            if muster.search(zeile):
                raise SystemExit(
                    "ABBRUCH: %s in src/%s.md, Zeile %d:\n  %s"
                    % (art, name, zeilennr, zeile.strip())
                )


def main():
    hier = os.path.dirname(os.path.abspath(__file__))
    for name, titel in SEITEN:
        quelle = os.path.join(hier, "src", name + ".md")
        md = io.open(quelle, encoding="utf-8").read()
        pruefen(name, md)
        nav = "".join(
            '<a href="%s.html"%s>%s</a>' % (n, ' class="hier"' if n == name else "", t)
            for n, t in SEITEN
        )
        seite = RAHMEN.format(titel=titel, navigation=nav, inhalt=md_to_html(md))
        io.open(os.path.join(hier, name + ".html"), "w", encoding="utf-8").write(seite)
        print("geschrieben: %s.html" % name)


if __name__ == "__main__":
    main()
