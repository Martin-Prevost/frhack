def detect_big_square(grid, i, j, size, value):
    for row in range(i, i + size):
        for col in range(j, j + size):
            if row >= len(grid) or col >= len(grid[0]) or grid[row][col] != value and grid[row][col] != value:
                return False
    return True

def replace_with_big_square(grid, i, j, size, value):
    for row in range(i, i + size):
        for col in range(j, j + size):
            grid[row][col] = value

def process_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            type_2, type_3 = 'b', 'c'
            if grid[i][j] == type_2 and detect_big_square(grid, i, j, 2, type_2):
                replace_with_big_square(grid, i, j, 2, 'B')
            elif grid[i][j] == type_3 and detect_big_square(grid, i, j, 3, type_3):
                replace_with_big_square(grid, i, j, 3, 'C')

# Exemple d'utilisation
grid = [
    ['a', 'a', 'a', 'b', 'a', 'a', 'a'],
    ['a', 'b', 'b', 'a', 'c', 'c', 'c'],
    ['a', 'b', 'b', 'a', 'c', 'c', 'c'],
    ['a', 'a', 'c', 'a', 'c', 'c', 'c']
]

print("Grille initiale :")
for row in grid:
    print(row)

process_grid(grid)

print("\nGrille après traitement :")
for row in grid:
    print(row)
