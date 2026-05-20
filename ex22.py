import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace (-100, 100, 100)
y = x**3 + 2 * x

plt.title ('Gráfico')
plt.xlabel ('Eixo X')
plt.ylabel ('Eixo Y')
plt.grid (True)
plt.plot (x, y, label = 'f(x) = x³ + 2x')
plt.legend()
plt.show()
