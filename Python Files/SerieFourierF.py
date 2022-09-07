
import matplotlib.pyplot as plt
import numpy as np

#funcion para fourier
def fourier(x):
	sum = 0
	# dependiendo las repeticiones (10)
	# será asi de cercano a la funcion cuadrada
	for i in range(1,10,2):
		sum += np.sin(i*x)/i
	return sum

		
# definimos el plot (graficacion)
x = np.arange(0,5,0.01)
# axis define el tamaño de la grafica
plt.axis([0, 5, -2, 2])
plt.plot(x, fourier(6*x))
plt.show()