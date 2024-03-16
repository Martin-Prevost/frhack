import json
import numpy as np
import pickle

grille, taille_grille = [], 0
with open('type.pkl', 'rb') as f:
    data = pickle.load(f)
    grille, len_x, len_y = data['grille'], data['len_x_grid'], data['len_y_grid']

traiter = [[False for _ in range(len_y)] for _ in range(len_x)]
grid = np.array(grille).reshape(len_x-1, len_y-1)
res = []

def detect_big_square(i, j, size, value):
    max_row, max_col = grid.shape
    for row in range(i, i + size):
        for col in range(j, j + size):
            if row >= max_row or col >= max_col or grid[row][col]['type'] != value:
                return False
    return True

def replace_with_big_square(i, j, size, value):
    sommet1 = grid[i][j]
    sommet2 = grid[i][j + size - 1]
    sommet4 = grid[i + size - 1][j]
    sommet3 = grid[i + size - 1][j + size - 1]
    dbm_somme = 0
    dbm_count = 0
    for row in range(i, i + size):
        for col in range(j, j + size):
            traiter[row][col] = True
            if grid[row][col]['dbm_moy'] != 0:
                dbm_somme += grid[row][col]['dbm_moy']
                dbm_count += len(grid[row][col]['releves'])

    dbm_moy = dbm_somme / dbm_count if dbm_count != 0 else 0.
    res.append({
        'sommet1_lambert': sommet1,
        'sommet2_lambert': sommet2,
        'sommet3_lambert': sommet3,
        'sommet4_lambert': sommet4,
        'dbm_moy': dbm_moy,
        'type': value
    })
    

def process_grid():
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if not traiter[i][j]:
                type_1, type_2, type_3 = 'URB', 'RUR', 'PERI'
                if grid[i][j]['type'] == type_2 and detect_big_square(i, j, 2, type_2):
                    replace_with_big_square(i, j, 2, type_2)
                elif grid[i][j]['type'] == type_3 and detect_big_square(i, j, 3, type_3):
                    replace_with_big_square(i, j, 3, type_3)
                elif grid[i][j]['type'] != type_1:
                    res.append(grid[i][j])

process_grid()

with open("etape3.pkl", "wb") as f:
    pickle.dump(res, f)