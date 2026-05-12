#!/usr/bin/env python3
"""
Sterbewahrscheinlichkeit nach Lebenshalbdekade - HTML Generator
Erzeugt eine HTML-Tabelle mit kumulativer Sterbewahrscheinlichkeit pro 5-Jahres-Halbdekade
für die Jahre 2016-2024, mit Männer und Frauen kombiniert.

Quelle: Österreichische Sterbetafeln 1947-2024
"""

import pandas as pd
import numpy as np

def generate_halfdeckade_html(csv_file, output_file):
    """
    Generiert HTML-Tabelle mit Sterbewahrscheinlichkeit nach Lebenshalbdekade.

    Args:
        csv_file: Pfad zur CSV-Datei mit Sterbetafeln
        output_file: Pfad für die Ausgabe HTML-Datei
    """

    # Lese CSV-Datei
    df = pd.read_csv(csv_file, delimiter=';')

    # Konvertiere Spalten zu numerischen Typen
    df['Alter'] = pd.to_numeric(df['Alter'], errors='coerce')
    df['Sterbewahrscheinlichkeit (q(x))'] = df['Sterbewahrscheinlichkeit (q(x))'].str.replace(',', '.').astype(float)
    df['Jahr'] = pd.to_numeric(df['Jahr'], errors='coerce')

    # Filtere Daten: Jahre 2016-2024
    filtered = df[(df['Jahr'] >= 2016) & (df['Jahr'] <= 2024)].copy()

    # Lebenshalbdekaden (5-Jahres-Intervalle) mit Correction für Alter 100+
    def get_halfdeckade(age):
        if pd.isna(age):
            return None
        age = int(age)
        if age >= 100:
            return "100+"
        return f"{(age // 5) * 5}-{(age // 5) * 5 + 4}"

    filtered['Lebenshalbdekade'] = filtered['Alter'].apply(get_halfdeckade)

    # Berechne kumulative Sterbewahrscheinlichkeit pro Halbdekade
    def calc_cumulative(group):
        """Berechne kumulative Sterbewahrscheinlichkeit über 5 Jahre"""
        group = group.sort_values('Alter')
        survival = np.prod(1 - group['Sterbewahrscheinlichkeit (q(x))'])
        return 1 - survival

    result = filtered.groupby(['Jahr', 'Lebenshalbdekade']).apply(calc_cumulative).reset_index()
    result.columns = ['Jahr', 'Lebenshalbdekade', 'Sterbewahrscheinlichkeit']

    pivot = result.pivot(index='Lebenshalbdekade', columns='Jahr', values='Sterbewahrscheinlichkeit')

    # Berechne kumulative Gesamtsterbewahrscheinlichkeit über alle Alter pro Jahr
    all_ages_total = filtered.groupby('Jahr').apply(
        lambda group: 1 - np.prod(1 - group['Sterbewahrscheinlichkeit (q(x))'])
    )
    pivot.loc['Alle Alter (Kumulativ)'] = all_ages_total

    # Definiere alle möglichen Halbdekaden
    halfdeckade_order = [f"{i}-{i+4}" for i in range(0, 100, 5)] + ["100+", "Alle Alter (Kumulativ)", "Alle Alter (0-100)"]

    # Berechne durchschnittliche Sterbewahrscheinlichkeit pro Jahr über alle einzelnen Alter (0-100)
    all_ages_avg = filtered.groupby('Jahr')['Sterbewahrscheinlichkeit (q(x))'].mean()
    pivot.loc['Alle Alter (0-100)'] = all_ages_avg

    # HTML-Tabelle erstellen
    html_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kumulative Sterbewahrscheinlichkeit pro Lebenshalbdekade 2016-2024</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 2200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }

        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
            font-size: 28px;
        }

        .subtitle {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 10px;
            font-size: 14px;
        }

        .info-box {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 13px;
            padding: 12px;
            background-color: #ecf0f1;
            border-radius: 6px;
            border-left: 4px solid #3498db;
        }

        .table-wrapper {
            overflow-x: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 10px;
        }

        thead {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            position: sticky;
            top: 0;
            z-index: 10;
        }

        th {
            padding: 7px 3px;
            text-align: center;
            font-weight: 600;
            border: 1px solid #bdc3c7;
            white-space: nowrap;
            min-width: 55px;
        }

        th.halfdeckade {
            text-align: left;
            min-width: 95px;
            padding-left: 12px;
        }

        th.year-header {
            background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
            font-weight: 700;
            font-size: 11px;
            padding: 9px 3px;
        }

        td {
            padding: 5px 3px;
            border: 1px solid #ecf0f1;
            text-align: center;
        }

        td.halfdeckade {
            text-align: left;
            font-weight: 600;
            background-color: #ecf0f1;
            padding-left: 12px;
            position: sticky;
            left: 0;
            z-index: 5;
        }

        td.no-data {
            background-color: #f5f5f5;
            color: #999;
            font-style: italic;
        }

        tr.total td {
            background-color: #f0f8ff !important;
            font-weight: bold;
            border-top: 3px solid #2c3e50;
            border-bottom: 3px solid #2c3e50;
        }

        tr.total td.halfdeckade {
            background-color: #d4e6f1 !important;
        }

        tbody tr:nth-child(odd) {
            background-color: #f8f9fa;
        }

        tbody tr:hover {
            background-color: #f0f0f0;
        }

        .value {
            font-weight: 600;
            color: #2c3e50;
            font-family: 'Courier New', monospace;
            font-size: 10px;
        }

        .change {
            font-size: 8px;
            margin-top: 1px;
            font-weight: 600;
        }

        .positive {
            color: #e74c3c;
        }

        .negative {
            color: #27ae60;
        }

        .neutral {
            color: #7f8c8d;
        }

        .legend {
            margin-top: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-left: 5px solid #2c3e50;
            border-radius: 8px;
        }

        .legend h3 {
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .legend-item {
            margin: 8px 0;
            color: #34495e;
            line-height: 1.6;
            font-size: 13px;
        }

        .info {
            margin-top: 20px;
            padding: 15px;
            background-color: #ecf0f1;
            border-radius: 4px;
            font-size: 13px;
            color: #2c3e50;
            line-height: 1.6;
        }

        .info ul {
            margin-left: 20px;
            margin-top: 10px;
        }

        .info li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Kumulative Sterbewahrscheinlichkeit pro Lebenshalbdekade</h1>
        <p class="subtitle">Österreich 2016-2024 | Männer und Frauen kombiniert</p>
        <div class="info-box">
            <strong>Hinweis:</strong> Die Werte zeigen die Wahrscheinlichkeit, dass eine Person während der gesamten 5-Jahre-Halbdekade verstirbt.
            <br/>Die Gruppe "100+" enthält nur Alter 100 (keine Daten für 101+ verfügbar)
        </div>

        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th class="halfdeckade">Alter</th>
"""

    # Header für Jahre
    for year in range(2016, 2025):
        html_content += f"""                        <th class="year-header" colspan="2">{year}</th>
"""

    html_content += """                    </tr>
                    <tr>
                        <th class="halfdeckade"></th>
"""

    # Sub-Header
    for year in range(2016, 2025):
        html_content += """                        <th>Wert %</th>
                        <th>Änd.%</th>
"""

    html_content += """                    </tr>
                </thead>
                <tbody>
"""

    # Fülle die Tabelle mit Daten
    years = list(range(2016, 2025))

    for halfdeckade in halfdeckade_order:
        row_data = pivot.loc[halfdeckade] if halfdeckade in pivot.index else None

        # Markiere "Alle Alter"-Zeile mit CSS-Klasse
        row_class = ' class="total"' if halfdeckade == "Alle Alter" else ''
        html_content += f"""                <tr{row_class}>
                    <td class="halfdeckade">{halfdeckade}</td>
"""

        for i, year in enumerate(years):
            if row_data is None or pd.isna(row_data.get(year, np.nan)):
                html_content += f"""                    <td class="no-data">—</td>
                    <td class="no-data">—</td>
"""
            else:
                value = row_data[year]
                value_percent = value * 100

                html_content += f"""                    <td class="value">{value_percent:.2f}%</td>
"""

                # Berechne Änderung zum Vorjahr (auch für 2024)
                if i > 0:
                    prev_year = years[i - 1]
                    prev_year_value = row_data.get(prev_year, np.nan)

                    if pd.notna(prev_year_value) and prev_year_value > 0:
                        change_pct = ((value - prev_year_value) / prev_year_value) * 100

                        if change_pct < -0.5:
                            color_class = "negative"
                            sign = "▼"
                        elif change_pct > 0.5:
                            color_class = "positive"
                            sign = "▲"
                        else:
                            color_class = "neutral"
                            sign = "="

                        html_content += f"""                    <td class="change"><span class="{color_class}">{sign} {change_pct:.2f}%</span></td>
"""
                    else:
                        html_content += f"""                    <td class="change">—</td>
"""
                else:
                    # Erstes Jahr: keine Änderung zum Vorjahr
                    html_content += f"""                    <td class="change">—</td>
"""

        html_content += """                </tr>
"""

    html_content += """                </tbody>
            </table>
        </div>

        <div class="legend">
            <h3>📝 Legende</h3>
            <div class="legend-item">
                <strong>Alter:</strong> 5-Jahres-Altersintervalle (z.B. 60-64 = Personen im Alter 60 bis 64 Jahre). Die Gruppe "100+" enthält nur Alter 100.
            </div>
            <div class="legend-item">
                <strong>Wert %:</strong> Kumulative Sterbewahrscheinlichkeit über die gesamte 5-Jahre-Halbdekade (z.B. 7,22% = Wahrscheinlichkeit, dass eine 60-jährige Person vor Alter 65 verstirbt)
            </div>
            <div class="legend-item">
                <strong>Änd.%:</strong> Prozentuale Veränderung zum Vorjahr
            </div>
            <div class="legend-item">
                <strong>▼ Grün:</strong> Verbesserung (niedrigere Sterbewahrscheinlichkeit)
            </div>
            <div class="legend-item">
                <strong>▲ Rot:</strong> Verschlechterung (höhere Sterbewahrscheinlichkeit)
            </div>
            <div class="legend-item">
                <strong>— Grau:</strong> Keine Daten für diesen Zeitraum verfügbar
            </div>
        </div>

        <div class="info">
            <strong>ℹ️ Wichtige Hinweise:</strong>
            <ul>
                <li><strong>Kumulative Wahrscheinlichkeit pro Halbdekade:</strong> 1 - [(1 - q(x)) × (1 - q(x+1)) × (1 - q(x+2)) × (1 - q(x+3)) × (1 - q(x+4))]</li>
                <li><strong>Altersgruppe "100+":</strong> Die Sterbetafeln enden bei Alter 100 - es gibt keine Daten für 101+. Daher zeigt "100+" nur die Jahressterbewahrscheinlichkeit für Alter 100.</li>
                <li><strong>Überlebenden-Effekt:</strong> Menschen über 100 Jahren sind eine sehr selektive Gruppe (nur die Gesündesten), daher können ihre Sterbewahrscheinlichkeiten etwas künstlich wirken.</li>
                <li>Männer und Frauen wurden kombiniert (Durchschnitt beider Geschlechter).</li>
                <li>Zeitraum: 2016-2024 (9 Jahre Datenreihe)</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

    # Speichere HTML-Datei
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ HTML-Tabelle erstellt: {output_file}")
    print(f"  Größe: {len(html_content):,} Bytes")


if __name__ == "__main__":
    # Standard-Pfade
    csv_file = "Sterbetafeln_1947_bis_2024.csv"
    output_file = "Sterbewahrscheinlichkeit_Lebenshalbdekaden_2016_2024.html"

    # Generiere HTML
    generate_halfdeckade_html(csv_file, output_file)

    print(f"\n✨ Fertig!")
    print(f"   CSV-Quelle: {csv_file}")
    print(f"   HTML-Output: {output_file}")
