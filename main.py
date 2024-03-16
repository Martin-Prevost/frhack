import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=';', dtype=None, names=True, encoding=None)

x = data['X']
y = data['Y']
puissance_dbm = data['dbm']

puissance_min = np.min(puissance_dbm)
puissance_max = np.max(puissance_dbm)

plt.scatter(x, y, c=puissance_dbm, cmap='RdYlGn', vmin=puissance_min, vmax=puissance_max)

cbar = plt.colorbar()
cbar.set_label('Puissance (dBm)')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Distribution des points en fonction de la puissance (dBm)')
plt.show()
