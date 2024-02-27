import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define os limites do retângulo
x = np.linspace(0, 2, 100)
y = np.linspace(0, 4, 100)

# Cria uma grade de coordenadas
X, Y = np.meshgrid(x, y)

# Calcula os valores da função (x+y)
Z = X + Y

# Cria uma figura tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plota o gráfico 3D da função
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Adiciona uma barra de cores
fig.colorbar(surf, label='(x+y)')

# Define os rótulos dos eixos
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('(x+y)')
ax.set_title('Gráfico tridimensional da função (x+y)')

plt.show()
