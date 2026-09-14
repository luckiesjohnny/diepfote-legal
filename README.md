# Rechtstexte zur App „Die Pfote"

Datenschutzerklärung, Impressum und Nutzungsbedingungen der Android-App **Die Pfote**,
veröffentlicht über GitHub Pages:

<https://luckiesjohnny.github.io/diepfote-legal/>

Dieses Repository ist öffentlich, weil es öffentlich sein muss: Google Play verlangt eine
Datenschutz-URL, die ohne Anmeldung erreichbar ist. Der Quellcode der App liegt woanders und
bleibt privat.

## Ändern

Die Markdown-Dateien unter `src/` sind Kopien aus dem App-Repository (Verzeichnis `legal/`).
Dort wird geändert, hierher kopiert, dann:

```
python3 build.py
```

Das schreibt die drei HTML-Seiten neu. `index.html` und `style.css` sind von Hand gepflegt und
werden nicht überschrieben.

Kein Jekyll, keine fremde Bibliothek, `.nojekyll` liegt bei: Ausgeliefert wird genau das, was
hier committet ist. Ein Rechtstext soll nicht davon abhängen, ob ein Build auf fremder
Infrastruktur durchläuft.
