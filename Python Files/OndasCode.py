import matplotlib.pyplot as plt
import numpy as np


# definimos el plot (graficacion)
x = np.arange(0,5,0.1)
plt.plot(x, np.sin(3*x))
plt.show()