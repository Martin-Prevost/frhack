import numpy as np
import json
from pyproj import Proj, transform

data = np.genfromtxt('data.csv', delimiter=';', dtype=str, skip_header=1)

ids = data[:, 0]
x = data[:, 1].astype(int)
y = data[:, 2].astype(int)
technos = data[:, 3]
operateurs = data[:, 4]
dbms = data[:, 5].astype(int)
puissances_recues = data[:, 6]

lambert93 = Proj(init='epsg:2154') # Lambert 93
wgs84 = Proj(init='epsg:4326') # WGS84 (lat/lon)

x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)

# Définir la taille de la grille et le nombre de cellules
grid_size = 50
x_grid = np.linspace(x_min, x_max, grid_size + 1)  # Ajoutez 1 à grid_size pour avoir le bon nombre de cellules
y_grid = np.linspace(y_min, y_max, grid_size + 1)

# Initialiser la matrice pour stocker les moyennes
average_power = np.full((grid_size, grid_size), np.nan)

grille = []

# Calculer la moyenne des points dans chaque cellule de la grille
for i in range(grid_size):
    print(i)
    for j in range(grid_size):
        x_lower, x_upper = float(x_grid[i]), float(x_grid[i + 1])
        y_lower, y_upper = float(y_grid[j]), float(y_grid[j + 1])
        indices = np.where((x >= x_lower) & (x < x_upper) & (y >= y_lower) & (y < y_upper))
        centre_lambert = (x_lower + x_upper) / 2, (y_lower + y_upper) / 2
        sommet1_lambert = (x_lower, y_upper)
        sommet2_lambert = (x_upper, y_upper)
        sommet3_lambert = (x_lower, y_lower)
        sommet4_lambert = (x_upper, y_lower)
        centre_gps = transform(lambert93, wgs84, (x_lower + x_upper) / 2, (y_lower + y_upper) / 2)
        if len(indices[0]) > 0:
            average_power[i, j] = np.mean(dbms[indices])
            releves = list(zip(ids[indices], [int(e) for e in dbms[indices]], technos[indices]))
            grille.append({
                'centre_lambert':centre_lambert,
                'sommet1_lambert': sommet1_lambert,
                'sommet2_lambert': sommet2_lambert,
                'sommet3_lambert': sommet3_lambert,
                'sommet4_lambert': sommet4_lambert,
                'centre_gps':centre_gps,
                'releves': releves,
                'dbm_moy': float(average_power[i, j]),
                'type': None})
        else:
            grille.append({
                'centre_lambert':centre_lambert,
                'sommet1_lambert': sommet1_lambert,
                'sommet2_lambert': sommet2_lambert,
                'sommet3_lambert': sommet3_lambert,
                'sommet4_lambert': sommet4_lambert,
                'centre_gps':centre_gps,
                'releves': [],
                'dbm_moy': 0,
                'type': None})            

# Enregistrer la grille au format JSON avec indentation
with open('grille.json', 'w') as f:
    json.dump({'grille': grille, 'taille_grille': grid_size}, f, indent=4)