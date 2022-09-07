import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# AQUI SE DEFINE EL TAMAÑO DE LA GRAFICACION
fig, ax = plt.subplots(2,1)

#PARAMETROS DE LA ONDA
amplitud = 10
longOnda = 2
faseInicial = np.pi
frecuencia1 = 0.1
#frecuencia2 = 0.2

# LA FORMA DE LA ONDA
x=np.arange(0,2*np.pi,0.01)

# FORMULA
linea1 = ax[0].plot(x, amplitud*np.sin (faseInicial+x*2*np.pi/longOnda+faseInicial))
#linea2 = ax[1].plot(x, amplitud*np.sin (faseInicial+x*2*np.pi/longOnda+faseInicial))


#def animacion (i):
 #   linea1[0].set_ydata(amplitud*np.sin (faseInicial+x*2*np.pi/longOnda+faseInicial+i*2*np.pi*frecuencia1))
 #   linea2[0].set_ydata(amplitud*np.sin (faseInicial+x*2*np.pi/longOnda+faseInicial+i*2*np.pi*frecuencia2))
    
   # return linea1,linea2

#ani = animation.FuncAnimation(fig, animacion, interval=100)

plt.show()