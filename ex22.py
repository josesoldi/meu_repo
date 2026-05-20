import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace (-10, 10, 100)
y = np.sin(x)

plt.title ('Gráfico')
plt.xlabel ('Eixo X')
plt.ylabel ('Eixo Y')
plt.grid (True)
plt.plot (x, y, label = 'f(x) = seno(x)')
plt.legend()
plt.show()
