import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

filename = "data/Mesures sur 41 45 89.csv"
dept_file = "data/Shape Depts 41 45 89.shp"
town_file = "data/Shape Blois Orleans Auxerre.shp"
peri_urbaines_file = "data/Zones PERI URBAINES 41 45 89.shp"
rurales_file = "data/Zones RURALES 41 45 89.shp"
urbaines_file = "data/Zones URBAINES 41 45 89.shp"

data = np.genfromtxt(filename, delimiter=';', dtype=str, skip_header=1)

size_urb = 1500
selected_operator = "OP1"
techno_list = ["4G", "5G", "all"]
selected_techno = techno_list[2]

if selected_techno != "all":
    data = data[data[:, 3] == selected_techno]

data = data[data[:, 4] == selected_operator]

ids = data[:, 0]
x = data[:, 1].astype(int)
y = data[:, 2].astype(int)
technos = data[:, 3]
operateurs = data[:, 4]
dbms = data[:, 5].astype(int)
puissances_recues = data[:, 6]

X_train = np.array([x, y]).T
y_train = dbms

print("Shape of X_train:", X_train.shape)
print("Shape of Y_train:", y_train.shape)

# Création du modèle k-NN avec noyau gaussien
knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(X_train, y_train)

# Generate a mesh grid
x_min, x_max = x.min() - 1, x.max() + 1
y_min, y_max = y.min() - 1, y.max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 1000),
                     np.arange(y_min, y_max, 1000))

# Predict on the mesh grid
Z = knn_regressor.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
print(Z)

# Plot the predicted values
plt.contourf(xx, yy, Z, alpha=0.8)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Kernel Ridge Regression')
plt.colorbar()
plt.show()




