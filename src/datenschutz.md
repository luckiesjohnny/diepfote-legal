# Datenschutzerklärung

Stand: 23. September 2026

## 1. Verantwortlicher

**Fabian Klemusch**
Wilhelm-Klein Straße 20, 51427 Bergisch Gladbach, Deutschland
E-Mail: finja.dogs@gmail.com

Einen Datenschutzbeauftragten haben wir nicht bestellt; die Voraussetzungen des § 38 BDSG
liegen nicht vor.

## 2. Der Grundsatz: Deine Daten bleiben auf deinem Gerät

Die Pfote hat **keine Benutzerkonten, keine Anmeldung und keinen Server**, auf dem deine Daten
liegen. Alles, was du erfasst — Hundeprofile, Impfungen, Medikationen, Gewichtsverlauf,
Rechnungen und Tierarzt-Favoriten — wird ausschließlich lokal auf deinem Gerät gespeichert, und
zwar verschlüsselt (AES-256-GCM, Schlüssel im Android-Keystore). Das Profilfoto deines Hundes
liegt als Bilddatei im privaten Speicherbereich der App, auf den andere Apps keinen Zugriff
haben, und ist dort durch die Geräteverschlüsselung von Android geschützt.

Wir haben keinen Zugriff auf diese Daten. Sie werden nicht an uns und nicht an Dritte
übertragen.

Die Speicherung auf deinem Endgerät ist für die Bereitstellung der von dir ausdrücklich
gewünschten Funktion unbedingt erforderlich im Sinne des § 25 Abs. 2 Nr. 2 TDDDG und daher
einwilligungsfrei.

## 3. Wann Daten das Gerät doch verlassen

Das geschieht in genau den fünf Fällen, die hier beschrieben sind. Bei jeder dieser Anfragen
erhält der Empfänger technisch bedingt auch die IP-Adresse deines Geräts.

### 3.1 Tierarztsuche und Notdienst-Umkreis (HERE Technologies)

**Was übertragen wird:** deine Standortkoordinaten, auf etwa 100 Meter gerundet (seit Version
1.29.2; vorher ungerundet), beziehungsweise dein eingegebener Suchbegriff (Ort, Postleitzahl).
Öffnest du eine Praxis, zusätzlich deren Koordinaten, um die Fahrzeit dorthin zu berechnen.
**An wen:** HERE Global B.V., Niederlande — Betreiber der genutzten Karten- und Ortsdienste.
**Wofür:** um Tierarztpraxen und Kliniken in deiner Umgebung zu finden, die Fahrzeit zu einer
Praxis zu schätzen, Koordinaten in einen Ortsnamen aufzulösen und zu bestimmen, welche
Landestierärztekammer für den tierärztlichen Notdienst an deinem Ort zuständig ist.
**Rechtsgrundlage:** Art. 6 Abs. 1 lit. b DSGVO (Erfüllung der von dir angeforderten Funktion).
Der Zugriff auf den Gerätestandort setzt zusätzlich deine Freigabe über die
Android-Berechtigung voraus; diese kannst du jederzeit in den Systemeinstellungen widerrufen.
**Was nicht übertragen wird:** keine Angaben zu dir, deinem Hund, deinen Rechnungen oder
Impfungen. Es besteht keine Kennung, über die sich deine Anfragen zu einem Profil
zusammenführen ließen.

### 3.2 Auflösen von Koordinaten in Ortsnamen (Android-Systemdienst)

Für die Umwandlung von Koordinaten in Orts- und Kreisnamen nutzt die App zunächst den in
Android eingebauten Dienst (`Geocoder`), ebenfalls mit auf etwa 100 Meter gerundeten
Koordinaten. Je nach Gerät und Hersteller wird diese Anfrage vom Betriebssystem an dessen
Anbieter — in der Regel Google Ireland Limited — weitergeleitet. Auf diese Verarbeitung haben
wir keinen Einfluss; sie erfolgt im Rahmen deines Betriebssystems.

### 3.3 Gassiwetter und Pfotenschutz-Ampel (Open-Meteo)

**Was übertragen wird:** die Koordinaten des Orts, für den du das Wetter siehst, auf etwa einen
Kilometer gerundet (seit Version 1.29.2; vorher auf etwa 11 Meter).
**An wen:** OpenMeteo GmbH, Hintere Schilligmatte 6, 6463 Bürglen (UR), Schweiz. Für die Schweiz
besteht ein Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO).
**Wofür:** um Temperatur, Sonneneinstrahlung, Niederschlag und Gewitter für die nächsten Stunden
abzurufen, aus denen die App die Asphalttemperatur und die Pfotenschutz-Ampel berechnet.
**Rechtsgrundlage:** Art. 6 Abs. 1 lit. b DSGVO (Erfüllung der von dir angeforderten Funktion).
**Beim Anbieter:** Nach eigenen Angaben speichert Open-Meteo IP-Adressen nur in Server-Protokollen
zur Wartung und gegen Missbrauch und löscht diese nach 90 Tagen.

### 3.4 Kauf von Die Pfote Plus und Update-Hinweis (Google Play)

**Was übertragen wird:** die Kaufabwicklung läuft vollständig über Google Play. Wir erhalten
weder deine Zahlungsdaten noch deinen Namen oder deine Adresse.
**An wen:** Google Ireland Limited als Betreiber von Google Play. Google ist zugleich dein
Vertragspartner für den Kauf.
**Wofür:** Abwicklung und Prüfung deiner Berechtigung.
**Rechtsgrundlage:** Art. 6 Abs. 1 lit. b DSGVO.
**Was die App lokal speichert:** die Art deines Kaufs (monatlich, jährlich, einmalig), ein von
Google vergebenes Kauf-Kennzeichen und der Zeitpunkt der letzten Bestätigung durch Google.
Dieses Kennzeichen dient ausschließlich dazu, die gekauften Funktionen freizuschalten — auch
dann, wenn dein Gerät gerade keine Verbindung hat.
**Update-Hinweis:** Beim Start fragt die App über die Play-Store-App deines Geräts ab, ob eine
neuere Version bereitsteht (Google Play In-App Updates). Die App selbst überträgt dabei nichts;
welche Daten der Play Store für diese Abfrage an Google übermittelt, richtet sich nach den
Datenschutzhinweisen von Google.

### 3.5 Diagnosedaten der Texterkennung (Google ML Kit)

Wenn du eine Rechnung oder einen Impfstoff-Aufkleber scannst, erkennt Google ML Kit den Text auf
deinem Gerät (siehe Abschnitt 4). **Bild und erkannter Text werden dabei nicht übertragen.**
ML Kit sendet aber technische Diagnose- und Nutzungsdaten an Google, und Google sieht nicht vor,
dass eine App das abschaltet.

**Was übertragen wird:** nach Angaben von Google Geräteinformationen (Hersteller, Modell,
Android-Version, verfügbare Rechenbeschleuniger), App-Informationen (Paketname, Version),
Leistungswerte wie die Verarbeitungsdauer, die Konfiguration der Erkennung (etwa Bildformat und
Auflösung), Fehlercodes sowie eine je Installation vergebene Kennung, die weder dich noch dein
Gerät eindeutig identifizieren soll. Bei der Rechnungsauswertung mit dem Sprachmodell Gemini Nano
kommen die eingestellten Sprachen hinzu.
**An wen:** Google LLC, USA. Google ist nach dem EU-US Data Privacy Framework zertifiziert.
**Wofür:** Fehlerdiagnose und Nutzungsauswertung der ML-Kit-Dienste durch Google.
**Rechtsgrundlage:** Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse ist eine
Texterkennung, die Rechnungen und Impfdaten auf dem Gerät auswertet, statt sie in eine Cloud zu
schicken.

## 4. Kamera, Fotos und die Auswertung von Rechnungen

Fotos, die du von einer Rechnung oder einem Impfstoff-Aufkleber aufnimmst oder aus deiner
Galerie auswählst, liest die App einmal aus und verwirft sie danach; eine Kamera-Aufnahme liegt
nur bis dahin im Zwischenspeicher der App. Gespeichert wird allein das Ergebnis — Praxis, Datum,
Positionen, Beträge beziehungsweise Präparat und Charge — in deiner verschlüsselten Akte.

Die Texterkennung und die Auswertung der Rechnung nach der Gebührenordnung für Tierärzte laufen
**vollständig auf deinem Gerät** (Google ML Kit, lokale Modelle). Bilder und erkannter Text
verlassen dein Gerät dabei nicht; zu den technischen Diagnosedaten, die ML Kit an Google sendet,
siehe Abschnitt 3.5. Vor der Auswertung entfernt die App personenbezogene Angaben aus dem
erkannten Text — unter anderem IBAN, Rechnungs- und Kundennummern sowie Namen.

Was von einer Rechnung in die Akte übernommen wird, bleibt lokal und verschlüsselt gespeichert,
bis du den Eintrag löschst.

## 5. Benachrichtigungen

Erinnerungen an fällige Impfungen und auslaufende Medikationen werden vollständig auf deinem
Gerät berechnet und dort als lokale Benachrichtigung angezeigt. Es findet keine Übertragung an
einen Server statt (kein Push-Dienst). Die Berechtigung für Benachrichtigungen kannst du
jederzeit in den Systemeinstellungen entziehen.

## 6. Was diese App nicht tut

- **Keine Analyse- oder Statistikdienste.** Kein Google Analytics, kein Firebase und keine
  eigene Nutzungsstatistik. Die Diagnosedaten, die Googles Texterkennung selbst erhebt, beschreibt
  Abschnitt 3.5.
- **Keine Absturzberichte an Dritte.**
- **Keine Werbung und kein Werbe-Tracking.** Es ist keine Werbe-Bibliothek eingebunden, und die
  Werbe-ID deines Geräts wird nicht ausgelesen.
- **Kein Verkauf und keine Weitergabe von Daten.** Auch nicht in anonymisierter Form.
- **Keine Profilbildung und keine automatisierte Entscheidungsfindung** im Sinne des Art. 22
  DSGVO.

## 7. Links zu fremden Seiten

Im Notfallbereich verweist die App auf die Notdienstportale der Landestierärztekammern. Ein
Antippen öffnet deinen Browser. Ab diesem Moment gilt die Datenschutzerklärung des jeweiligen
Anbieters; wir übertragen dabei nichts außer dem Seitenaufruf selbst, den dein Browser
ausführt.

## 8. Speicherdauer und Löschung

Deine Daten bleiben so lange auf deinem Gerät, wie du sie dort behältst. Du löschst sie, indem
du einzelne Einträge entfernst, die App-Daten in den Android-Einstellungen löschst oder die App
deinstallierst. Danach sind sie unwiederbringlich fort — wir halten keine Kopie vor und können
nichts wiederherstellen. Wenn du Datenverlust vermeiden willst, lege eine Sicherung an.

## 9. Deine Rechte

Dir stehen nach der DSGVO das Recht auf Auskunft (Art. 15), Berichtigung (Art. 16), Löschung
(Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und
Widerspruch (Art. 21) zu.

In der Praxis kannst du diese Rechte unmittelbar selbst ausüben, denn die Daten liegen
ausschließlich bei dir: Du siehst sie vollständig in der App, kannst sie dort ändern und
löschen und mit Die Pfote Plus über die Sicherungsfunktion in einem maschinenlesbaren Format
ausleiten. Für
Anliegen, die darüber hinausgehen, erreichst du uns unter finja.dogs@gmail.com.

Unabhängig davon steht dir ein Beschwerderecht bei einer Datenschutz-Aufsichtsbehörde zu
(Art. 77 DSGVO), in der Regel bei der Behörde deines Wohnsitzlandes.

## 10. Änderungen dieser Erklärung

Wir passen diese Erklärung an, wenn sich die App ändert. Maßgeblich ist die jeweils in der App
und unter https://luckiesjohnny.github.io/diepfote-legal/datenschutz.html veröffentlichte
Fassung.
