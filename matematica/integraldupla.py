import numpy as np
import matplotlib.pyplot as plt

# Define os limites do retângulo
x = np.linspace(0, 2, 100)
y = np.linspace(0, 4, 100)

# Cria uma grade de coordenadas
X, Y = np.meshgrid(x, y)

# Calcula os valores da função (x+y)
Z = X + Y

# Plota o gráfico da função e o retângulo
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='(x+y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função (x+y) sobre o retângulo [0,2] x [0,4]')
plt.grid(True)
plt.show()
