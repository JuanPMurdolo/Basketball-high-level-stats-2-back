import csv
from typing import List, Dict, Any

def process_csv(filepath: str) -> Dict[str, Any]:
    """
    Procesa el archivo CSV de estadísticas de partido y retorna la información formateada.
    """
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    teams = []
    i = 0
    while i < len(rows):
        row = rows[i]
        # Detecta el inicio de una tabla de equipo
        if row and any("MM" in cell for cell in row):
            team_name = row[0].strip()
            # Busca encabezado de columnas
            while i < len(rows) and not rows[i][0].startswith("Num."):
                i += 1
            headers = rows[i]
            i += 1
            players = []
            # Procesa jugadores hasta encontrar 'TOTALES'
            while i < len(rows) and not (rows[i][0].startswith("TOTALES")):
                if rows[i][0].isdigit():
                    player_data = dict(zip(headers, rows[i]))
                    players.append(player_data)
                i += 1
            # Procesa totales de equipo
            if i < len(rows) and rows[i][0].startswith("TOTALES"):
                totals = dict(zip(headers, rows[i]))
                i += 1
            else:
                totals = {}
            teams.append({
                "team_name": team_name,
                "players": players,
                "totals": totals
            })
        else:
            i += 1
    return {"teams": teams}

# Ejemplo de uso:
# stats = process_csv('/Users/juanpmurdolo/Downloads/estadisticaPartido_202411412 - Estadisticas.csv')
# print(stats)