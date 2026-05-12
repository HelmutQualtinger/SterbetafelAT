# Österreichische Sterbetafeln 1947-2024 - Analyse

Analyse der österreichischen Sterbetafeln mit Fokus auf kumulative Sterbewahrscheinlichkeiten pro Lebenshalbdekade (5-Jahres-Intervalle) für die Jahre 2016-2024.

## 📊 Dateien

- **Sterbetafeln_1947_bis_2024.csv** - Rohdaten aus den österreichischen Sterbetafeln (CSV-Format)
- **generate_html_halfdeckades.py** - Python-Skript zur Generierung der HTML-Tabelle
- **Sterbewahrscheinlichkeit_Lebenshalbdekaden_2016_2024.html** - Generierte HTML-Tabelle mit interaktiver Darstellung

## 🚀 Verwendung

### Voraussetzungen
- Python 3.x
- pandas
- numpy

### Installation
```bash
pip install pandas numpy
```

### HTML-Tabelle generieren
```bash
python3 generate_html_halfdeckades.py
```

Dies erzeugt die Datei `Sterbewahrscheinlichkeit_Lebenshalbdekaden_2016_2024.html`.

## 📈 Daten

Die Analyse zeigt:
- **Kumulative Sterbewahrscheinlichkeit** pro 5-Jahres-Halbdekade
- **Prozentuale Änderungen** zum Vorjahr
- **Kombinierte Daten** für Männer und Frauen
- **Zeitraum:** 2016-2024 (9 Jahre)
- **Altersgruppen:** 0-4 bis 95-99 Jahre, plus 100+

## 📊 Beispielwerte (2024)

| Altersgruppe | Sterbewahrscheinlichkeit | Änderung 2023→2024 |
|---|---|---|
| 20-24 | 0,37% | +1,35% |
| 40-44 | 1,09% | +8,56% |
| 60-64 | 6,85% | -5,05% |
| 70-74 | 17,21% | -4,54% |
| 80-84 | 42,56% | -2,01% |
| 90-94 | 88,54% | -1,74% |

## 🔍 Hinweise

- Die Gruppe "100+" enthält nur Alter 100 (keine Daten für 101+ verfügbar)
- Männer und Frauen wurden kombiniert (Durchschnitt)
- **Survivor Bias:** Menschen über 100 sind eine sehr selektive Gruppe
- Kumulative Wahrscheinlichkeit: 1 - [(1-q(x)) × (1-q(x+1)) × (1-q(x+2)) × (1-q(x+3)) × (1-q(x+4))]

## 📝 Quelle

Österreichische Sterbetafeln 1947-2024
