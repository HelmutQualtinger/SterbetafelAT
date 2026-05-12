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

## 📊 Sterblichkeitstabelle 2016–2024

| Altersgruppe | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|
| 0-4 | — | — | — | — | — | — | — | — | — |
| 5-9 | 0,08% | 0,06% | 0,07% | 0,07% | 0,06% | 0,06% | 0,08% | 0,07% | 0,09% |
| 10-14 | 0,08% | 0,09% | 0,08% | 0,10% | 0,09% | 0,07% | 0,11% | 0,09% | 0,06% |
| 15-19 | 0,29% | 0,27% | 0,27% | 0,26% | 0,28% | 0,29% | 0,31% | 0,36% | 0,33% |
| 20-24 | 0,35% | 0,31% | 0,35% | 0,35% | 0,32% | 0,38% | 0,38% | 0,37% | 0,37% |
| 25-29 | 0,38% | 0,40% | 0,39% | 0,40% | 0,32% | 0,38% | 0,41% | 0,37% | 0,39% |
| 30-34 | 0,51% | 0,46% | 0,50% | 0,52% | 0,52% | 0,52% | 0,49% | 0,49% | 0,52% |
| 35-39 | 0,65% | 0,67% | 0,68% | 0,65% | 0,66% | 0,74% | 0,73% | 0,74% | 0,78% |
| 40-44 | 1,03% | 1,01% | 1,11% | 1,00% | 1,08% | 1,05% | 1,04% | 1,01% | 1,09% |
| 45-49 | 1,71% | 1,62% | 1,67% | 1,71% | 1,55% | 1,72% | 1,61% | 1,66% | 1,55% |
| 50-54 | 2,80% | 2,83% | 2,75% | 2,58% | 2,67% | 2,85% | 2,59% | 2,55% | 2,43% |
| 55-59 | 4,93% | 4,74% | 4,87% | 4,39% | 4,57% | 4,55% | 4,41% | 4,14% | 4,07% |
| 60-64 | 7,87% | 7,64% | 7,49% | 7,22% | 7,60% | 7,93% | 7,70% | 7,22% | 6,85% |
| 65-69 | 12,46% | 11,88% | 12,00% | 11,80% | 12,01% | 12,57% | 12,18% | 11,22% | 11,17% |
| 70-74 | 18,22% | 18,51% | 18,44% | 18,08% | 19,29% | 19,52% | 18,64% | 18,03% | 17,21% |
| 75-79 | 26,89% | 26,67% | 26,56% | 26,29% | 29,44% | 29,43% | 29,39% | 28,52% | 27,61% |
| 80-84 | 44,68% | 45,15% | 44,44% | 43,09% | 46,13% | 44,88% | 44,99% | 43,43% | 42,56% |
| 85-89 | 68,91% | 70,23% | 69,14% | 68,41% | 71,50% | 70,37% | 70,91% | 68,38% | 66,33% |
| 90-94 | 88,74% | 89,73% | 89,94% | 89,48% | 91,09% | 90,13% | 91,05% | 90,11% | 88,54% |
| 95-99 | 97,97% | 98,03% | 97,93% | 97,66% | 98,23% | 98,31% | 98,82% | 98,08% | 97,57% |
| 100+ | — | 68,60% | 65,80% | 69,56% | 68,51% | 67,83% | 71,16% | 68,18% | 67,46% |
| **Alle Alter (0–100)** | **4,04%** | **4,53%** | **4,47%** | **4,41%** | **4,68%** | **4,62%** | **4,81%** | **4,51%** | **4,31%** |

## 📈 Jährliche Veränderungen (% zum Vorjahr)

| Altersgruppe | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|
| 0-4 | — | — | — | — | — | — | — | — | — |
| 5-9 | — | -27,70% | <span style="color: red; font-weight: bold;">+21,66%</span> | -1,37% | -13,89% | -6,45% | <span style="color: red; font-weight: bold;">+34,47%</span> | -8,97% | <span style="color: red; font-weight: bold;">+23,93%</span> |
| 10-14 | — | <span style="color: red; font-weight: bold;">+19,22%</span> | -18,27% | <span style="color: red; font-weight: bold;">+27,62%</span> | -8,24% | -23,59% | <span style="color: red; font-weight: bold;">+55,85%</span> | -10,37% | -31,57% |
| 15-19 | — | -7,52% | -1,11% | -1,87% | <span style="color: red; font-weight: bold;">+6,10%</span> | <span style="color: red; font-weight: bold;">+6,11%</span> | <span style="color: red; font-weight: bold;">+5,41%</span> | <span style="color: red; font-weight: bold;">+15,09%</span> | -6,41% |
| 20-24 | — | -11,35% | <span style="color: red; font-weight: bold;">+11,20%</span> | <span style="color: red; font-weight: bold;">+0,57%</span> | -7,44% | <span style="color: red; font-weight: bold;">+18,55%</span> | <span style="color: red; font-weight: bold;">+0,26%</span> | -3,64% | <span style="color: red; font-weight: bold;">+1,35%</span> |
| 25-29 | — | <span style="color: red; font-weight: bold;">+7,15%</span> | -2,47% | <span style="color: red; font-weight: bold;">+0,76%</span> | -18,36% | <span style="color: red; font-weight: bold;">+17,87%</span> | <span style="color: red; font-weight: bold;">+8,36%</span> | -10,13% | <span style="color: red; font-weight: bold;">+4,30%</span> |
| 30-34 | — | -10,72% | <span style="color: red; font-weight: bold;">+10,26%</span> | <span style="color: red; font-weight: bold;">+4,36%</span> | -1,33% | <span style="color: red; font-weight: bold;">+1,16%</span> | -6,84% | -0,20% | <span style="color: red; font-weight: bold;">+6,33%</span> |
| 35-39 | — | <span style="color: red; font-weight: bold;">+2,60%</span> | <span style="color: red; font-weight: bold;">+1,49%</span> | -3,96% | <span style="color: red; font-weight: bold;">+1,07%</span> | <span style="color: red; font-weight: bold;">+11,93%</span> | -1,08% | <span style="color: red; font-weight: bold;">+1,22%</span> | <span style="color: red; font-weight: bold;">+6,20%</span> |
| 40-44 | — | -1,73% | <span style="color: red; font-weight: bold;">+9,97%</span> | -10,49% | <span style="color: red; font-weight: bold;">+8,15%</span> | -2,39% | -1,69% | -2,78% | <span style="color: red; font-weight: bold;">+8,56%</span> |
| 45-49 | — | -5,23% | <span style="color: red; font-weight: bold;">+2,85%</span> | <span style="color: red; font-weight: bold;">+2,47%</span> | -9,73% | <span style="color: red; font-weight: bold;">+11,35%</span> | -6,64% | <span style="color: red; font-weight: bold;">+3,62%</span> | -7,05% |
| 50-54 | — | <span style="color: red; font-weight: bold;">+0,83%</span> | -2,83% | -5,97% | <span style="color: red; font-weight: bold;">+3,41%</span> | <span style="color: red; font-weight: bold;">+6,50%</span> | -8,98% | -1,44% | -4,90% |
| 55-59 | — | -3,82% | <span style="color: red; font-weight: bold;">+2,64%</span> | -9,77% | <span style="color: red; font-weight: bold;">+4,07%</span> | -0,41% | -3,11% | -6,13% | -1,72% |
| 60-64 | — | -3,00% | -1,97% | -3,50% | <span style="color: red; font-weight: bold;">+5,24%</span> | <span style="color: red; font-weight: bold;">+4,35%</span> | -2,88% | -6,35% | -5,05% |
| 65-69 | — | -4,65% | <span style="color: red; font-weight: bold;">+0,99%</span> | -1,66% | <span style="color: red; font-weight: bold;">+1,77%</span> | <span style="color: red; font-weight: bold;">+4,70%</span> | -3,11% | -7,91% | -0,38% |
| 70-74 | — | <span style="color: red; font-weight: bold;">+1,58%</span> | -0,37% | -1,94% | <span style="color: red; font-weight: bold;">+6,65%</span> | <span style="color: red; font-weight: bold;">+1,21%</span> | -4,52% | -3,27% | -4,54% |
| 75-79 | — | -0,80% | -0,43% | -1,04% | <span style="color: red; font-weight: bold;">+12,01%</span> | -0,03% | -0,16% | -2,95% | -3,20% |
| 80-84 | — | <span style="color: red; font-weight: bold;">+1,05%</span> | -1,57% | -3,04% | <span style="color: red; font-weight: bold;">+7,05%</span> | -2,72% | <span style="color: red; font-weight: bold;">+0,25%</span> | -3,46% | -2,01% |
| 85-89 | — | <span style="color: red; font-weight: bold;">+1,91%</span> | -1,54% | -1,06% | <span style="color: red; font-weight: bold;">+4,52%</span> | -1,59% | <span style="color: red; font-weight: bold;">+0,77%</span> | -3,57% | -3,00% |
| 90-94 | — | <span style="color: red; font-weight: bold;">+1,11%</span> | <span style="color: red; font-weight: bold;">+0,24%</span> | -0,51% | <span style="color: red; font-weight: bold;">+1,79%</span> | -1,05% | <span style="color: red; font-weight: bold;">+1,03%</span> | -1,04% | -1,74% |
| 95-99 | — | <span style="color: red; font-weight: bold;">+0,07%</span> | -0,11% | -0,27% | <span style="color: red; font-weight: bold;">+0,59%</span> | <span style="color: red; font-weight: bold;">+0,08%</span> | <span style="color: red; font-weight: bold;">+0,52%</span> | -0,75% | -0,53% |
| 100+ | — | — | -4,09% | <span style="color: red; font-weight: bold;">+5,71%</span> | -1,50% | -1,00% | <span style="color: red; font-weight: bold;">+4,91%</span> | -4,18% | -1,05% |
| **Alle Alter (0–100)** | — | **<span style="color: red; font-weight: bold;">+12,01%</span>** | **-1,31%** | **-1,32%** | **<span style="color: red; font-weight: bold;">+6,04%</span>** | **-1,23%** | **<span style="color: red; font-weight: bold;">+4,10%</span>** | **-6,31%** | **-4,41%** |

## ⚖️ Gewichtete Durchschnittliche Änderungen

Die folgende Tabelle zeigt die **gewichteten Durchschnitte der Sterblichkeitsänderungen**, gewichtet nach den Sterbewahrscheinlichkeiten der jeweiligen Altersgruppen (2024-Baseline). Dies berücksichtigt, dass Veränderungen in älteren Altersgruppen (höhere Mortalität) einen größeren Einfluss auf die Gesamtsterblichkeit haben.

| Jahr | Gewichtete Änderung | Trend |
|---|---|---|
| 2017 | <span style="color: red; font-weight: bold;">+0,48%</span> | Leichte Verschlechterung |
| 2018 | -0,97% | Verbesserung |
| 2019 | -0,12% | Leichte Verbesserung |
| 2020 | <span style="color: red; font-weight: bold;">+2,80%</span> | 🔴 **Pandemiespitze** |
| 2021 | -0,50% | Leichte Verbesserung |
| 2022 | <span style="color: red; font-weight: bold;">+0,82%</span> | Erhöhte Sterblichkeit |
| 2023 | -2,58% | 🟢 **Starke Erholung** |
| 2024 | -1,78% | 🟢 Anhaltendes Absinken |

**Interpretation:** Die gewichteten Daten zeigen deutlich, dass 2020 mit +2,80% das schlimmste Jahr war (Pandemie), während 2023–2024 die stärksten Verbesserungen zeigen (–2,58% und –1,78%). Dies spiegelt die altersabhängige Mortalitätsbelastung wider – ältere Menschen sind am stärksten von der Pandemie betroffen und deren Erholung ist auch am deutlichsten.

## 📉 Analyse und Ergebnisse

Die Daten zeigen ein klares Bild in drei Phasen:

**Vor Pandemie (2016–2019):** Gesamtrate schwankt zwischen 4,04% und 4,53%, leicht rückläufiger Trend – normale Sterblichkeitsverbesserung durch medizinischen Fortschritt.

**Pandemie (2020–2022):** Die Gesamtrate springt auf Ø 4,70% – ein Anstieg von ~8% gegenüber der Baseline. Besonders auffällig: Die Altersgruppen 70–84 zeigen die stärksten absoluten Exzesse, mit +12% bei 75–79 im Jahr 2020. Der Pandemieeffekt ist eindeutig altersselektiv – unter 50 kaum messbar, ab 65 stark. 2022 ist mit 4,81% das schlimmste Jahr der gesamten Reihe.

**Post-Pandemie (2023–2024):** Rascher Rückgang auf 4,51% (2023) und 4,31% (2024) – das letzte Wert ist der niedrigste der gesamten 9-Jahres-Reihe. Das deutet auf einen kombinierten Effekt hin: einerseits Normalisierung nach Pandemie, andererseits möglicherweise ein "Harvesting"-Effekt (die vulnerablen Personen, die 2020–2022 verstorben sind, fehlen nun in der Risikogruppe), plus echte Sterblichkeitsverbesserung.

Der untere Chart macht das Muster bei den mittleren Altersgruppen 55–74 sehr deutlich: rote Balken während der Pandemie, grüne Balken danach – teils deutlich unter der Vorpandemiebasis.

## 🔍 Hinweise

- Die Gruppe "100+" enthält nur Alter 100 (keine Daten für 101+ verfügbar)
- Männer und Frauen wurden kombiniert (Durchschnitt)
- **Survivor Bias:** Menschen über 100 sind eine sehr selektive Gruppe
- Kumulative Wahrscheinlichkeit: 1 - [(1-q(x)) × (1-q(x+1)) × (1-q(x+2)) × (1-q(x+3)) × (1-q(x+4))]

## 📝 Quelle

Österreichische Sterbetafeln 1947-2024
