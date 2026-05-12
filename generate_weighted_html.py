#!/usr/bin/env python3
"""Generate HTML visualization of weighted average mortality changes."""

html_content = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gewichtete Sterblichkeitsänderungen 2017-2024</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
            max-width: 1200px;
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
            margin-bottom: 20px;
            font-size: 14px;
        }

        .info-box {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
            font-size: 13px;
            padding: 15px;
            background-color: #ecf0f1;
            border-radius: 6px;
            border-left: 4px solid #3498db;
            line-height: 1.6;
        }

        .chart-container {
            position: relative;
            height: 400px;
            margin-bottom: 40px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
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
            font-size: 14px;
        }

        thead {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            position: sticky;
            top: 0;
            z-index: 10;
        }

        th {
            padding: 12px;
            text-align: center;
            font-weight: 600;
            border: 1px solid #bdc3c7;
        }

        th.year {
            text-align: left;
            min-width: 100px;
        }

        td {
            padding: 12px;
            border: 1px solid #ecf0f1;
            text-align: center;
        }

        td.year {
            text-align: left;
            font-weight: 600;
            background-color: #ecf0f1;
            min-width: 100px;
        }

        .positive {
            color: #e74c3c;
            font-weight: bold;
        }

        .negative {
            color: #27ae60;
            font-weight: bold;
        }

        tbody tr:nth-child(odd) {
            background-color: #f8f9fa;
        }

        tbody tr:hover {
            background-color: #f0f0f0;
        }

        .interpretation {
            margin-top: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-left: 5px solid #2c3e50;
            border-radius: 8px;
        }

        .interpretation h3 {
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .interpretation p {
            color: #34495e;
            line-height: 1.8;
            margin: 10px 0;
        }

        .phase {
            margin: 15px 0;
            padding: 10px;
            background-color: rgba(255,255,255,0.3);
            border-radius: 4px;
        }

        .legend {
            display: flex;
            gap: 30px;
            justify-content: center;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
        }

        .legend-box {
            width: 20px;
            height: 20px;
            border-radius: 3px;
        }

        .legend-red {
            background-color: #e74c3c;
        }

        .legend-green {
            background-color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Gewichtete Sterblichkeitsänderungen 2017–2024</h1>
        <p class="subtitle">Österreich | Gewichtet nach Sterbewahrscheinlichkeit der Altersgruppen (2024-Baseline)</p>

        <div class="info-box">
            <strong>Methode:</strong> Die Änderungen jeder Altersgruppe werden mit ihrer Sterbewahrscheinlichkeit (2024) gewichtet.
            Dies berücksichtigt, dass ältere Menschen eine höhere Mortalität haben und deren Sterblichkeitstrends
            daher stärker zur Gesamtrate beitragen. So werden Veränderungen in den Altersgruppen 75–99 stärker gewichtet als in den Gruppen 20–49.
        </div>

        <div class="chart-container">
            <canvas id="trendsChart"></canvas>
        </div>

        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th class="year">Jahr</th>
                        <th>Gewichtete Änderung (%)</th>
                        <th>Trend</th>
                        <th>Interpretation</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="year">2017</td>
                        <td><span class="positive">+0,48%</span></td>
                        <td>↗️ Leicht verschlechtert</td>
                        <td>Geringfügiger Anstieg der Sterblichkeit</td>
                    </tr>
                    <tr>
                        <td class="year">2018</td>
                        <td><span class="negative">-0,97%</span></td>
                        <td>↘️ Verbesserung</td>
                        <td>Sterblichkeit sinkt – normaler medizinischer Fortschritt</td>
                    </tr>
                    <tr>
                        <td class="year">2019</td>
                        <td><span class="negative">-0,12%</span></td>
                        <td>↘️ Leicht besser</td>
                        <td>Baseline-Jahr vor Pandemie – stabile Verbesserung</td>
                    </tr>
                    <tr style="background-color: #ffe6e6;">
                        <td class="year"><strong>2020</strong></td>
                        <td><strong><span class="positive">+2,80%</span></strong></td>
                        <td>🔴 <strong>Pandemiespitze</strong></td>
                        <td><strong>Schlimmstes Jahr:</strong> Excess Mortality durch COVID-19 und Collateral Damage</td>
                    </tr>
                    <tr>
                        <td class="year">2021</td>
                        <td><span class="negative">-0,50%</span></td>
                        <td>↘️ Erste Erholung</td>
                        <td>Leichte Verbesserung trotz Pandemie – Impfungen wirken</td>
                    </tr>
                    <tr style="background-color: #ffe6e6;">
                        <td class="year">2022</td>
                        <td><span class="positive">+0,82%</span></td>
                        <td>↗️ Wieder erhöht</td>
                        <td>Pandemie-Nachwirkungen und neue Varianten – zweite Welle im Sommer 2022</td>
                    </tr>
                    <tr style="background-color: #e6ffe6;">
                        <td class="year"><strong>2023</strong></td>
                        <td><strong><span class="negative">-2,58%</span></strong></td>
                        <td>🟢 <strong>Starke Erholung</strong></td>
                        <td><strong>Beste Verbesserung:</strong> Normalisierung nach Pandemie + Harvesting-Effekt</td>
                    </tr>
                    <tr style="background-color: #e6ffe6;">
                        <td class="year">2024</td>
                        <td><span class="negative">-1,78%</span></td>
                        <td>🟢 Anhaltendes Absinken</td>
                        <td>Erholung setzt sich fort – niedrigste Gesamtrate der 9-Jahres-Reihe (4,31%)</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="interpretation">
            <h3>🔍 Interpretation der Pandemie-Phasen</h3>

            <div class="phase">
                <strong>Vor Pandemie (2017–2019):</strong><br>
                Gewichtete Änderungen zwischen –0,97% und +0,48%. Der Trend ist positiv (Verbesserung),
                typisch für medizinischen Fortschritt. Die hohen Gewichte (75–99 Jahre) treiben diese Verbesserungen an.
            </div>

            <div class="phase">
                <strong>Pandemie (2020–2022):</strong><br>
                <strong>2020:</strong> +2,80% – Disaster-Jahr. Die Pandemie trifft besonders ältere Menschen stark.
                Altersgruppen 75–84 zeigen +12%, die massivste Übersterblichkeit der Reihe.<br>
                <strong>2021:</strong> –0,50% – Verbesserung dank Impfungen, aber Pandemie hält an.<br>
                <strong>2022:</strong> +0,82% – Rückfall durch Omikron-Variante und Herbst/Winter-Infektionen.
            </div>

            <div class="phase">
                <strong>Erholung (2023–2024):</strong><br>
                <strong>2023:</strong> –2,58% – Beste Verbesserung in der ganzen Serie. Kombination aus:
                (a) Rückgang zu normaler Sterblichkeit, (b) Harvesting-Effekt (vulnerablste Personen bereits 2020–2022 verstorben),
                (c) Verbesserte Gesundheitsversorgung.<br>
                <strong>2024:</strong> –1,78% – Trend setzt sich fort. Gesamtsterblichkeitsrate ist nun niedriger als 2016.
            </div>

            <div style="margin-top: 15px; padding: 10px; background-color: rgba(255,255,255,0.3); border-radius: 4px;">
                <strong>Warum Gewichtung wichtig ist:</strong><br>
                Ohne Gewichtung würden Schwankungen in den Altersgruppen 15–19 (0,33% Mortalität)
                gleich zählen wie in 80–84 (42,56% Mortalität). Mit Gewichtung sehen wir, dass die Pandemie
                primär eine Katastrophe für Ältere war (+2,80% gewichtet vs. kleineren Schwankungen in jungen Gruppen).
            </div>
        </div>

        <div style="margin-top: 30px; padding: 20px; background-color: #f0f8ff; border-radius: 8px; border-left: 4px solid #2c3e50;">
            <strong>📝 Datenquelle:</strong> Österreichische Sterbetafeln 1947–2024.
            Gewichtung basiert auf 2024 kumulative Sterbewahrscheinlichkeiten pro 5-Jahres-Altersgruppe.
        </div>
    </div>

    <script>
        const ctx = document.getElementById('trendsChart').getContext('2d');

        const data = {
            labels: ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
            datasets: [{
                label: 'Gewichtete Sterblichkeitsänderung (%)',
                data: [0.48, -0.97, -0.12, 2.80, -0.50, 0.82, -2.58, -1.78],
                borderColor: '#2c3e50',
                backgroundColor: [
                    '#e74c3c',  // 2017 - red
                    '#27ae60',  // 2018 - green
                    '#27ae60',  // 2019 - green
                    '#c0392b',  // 2020 - dark red (pandemic)
                    '#27ae60',  // 2021 - green
                    '#e74c3c',  // 2022 - red
                    '#229954',  // 2023 - dark green
                    '#27ae60',  // 2024 - green
                ],
                borderWidth: 2,
                fill: false,
                tension: 0.4,
                pointRadius: 6,
                pointHoverRadius: 8,
                pointBackgroundColor: [
                    '#e74c3c', '#27ae60', '#27ae60', '#c0392b', '#27ae60', '#e74c3c', '#229954', '#27ae60'
                ]
            }]
        };

        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        labels: {
                            font: { size: 13 },
                            padding: 15
                        }
                    },
                    title: {
                        display: true,
                        text: 'Trend: Gewichtete Sterblichkeitsänderungen 2017–2024',
                        font: { size: 15, weight: 'bold' }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Änderung (%)',
                            font: { weight: 'bold' }
                        },
                        grid: {
                            color: 'rgba(0, 0, 0, 0.1)',
                            drawBorder: true
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Jahr',
                            font: { weight: 'bold' }
                        },
                        grid: {
                            display: false
                        }
                    }
                }
            }
        };

        new Chart(ctx, config);
    </script>
</body>
</html>
"""

with open('Gewichtete_Sterblichkeit_2017_2024.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ HTML-Datei erstellt: Gewichtete_Sterblichkeit_2017_2024.html")
