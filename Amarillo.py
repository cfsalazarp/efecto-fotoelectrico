
#Integrantes:
#Luisa Fernanda Torregrosa Serrato - 20152005054
#Daniel Valencia Gómez - 20161005027
#Christian Salazar Piñeros - 20161005082

# EXPERIMENTO EFECTO FOTOELECTRICO (AMARILLO) #

#Se importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

fig,ax = plt.subplots(figsize=(16,9))
fig.canvas.set_window_title('Experimento Filtro Amarillo')  

#Se ingresan los datos de voltaje (x) y corriente (y) obtenidos
#experimentalmente en el laboratorio
x = np.array([0,-0.1,-0.15,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8])
y = np.array([0.3,0.2,0,-0.2,-0.4,-0.5,-0.7,-0.8,-1,-1.2])

#Se realiza un ajuste polinomial de grado 2
z = np.polyfit(x, y, 2)
p = np.poly1d(z)

#Se ajusta el vector arrojado en z para cuadrar el polinomio
z4=z[0]
z3=z[1]
z2=z[2]
#Se obtiene el polinomio de ajuste
plt.text(-1.2,0.3, 'El polinomio de ajuste es:', fontsize = 10)
plt.text(-1.2,0.2, r'$%0.3fx^2+%0.3fx+%0.3f$'
         %(z4,z3,z2),fontsize=13)

#Se resuelve el polinomio para hallar el voltaje de frenado
def f(x):
    return (z4*x**2)+(z3*x)+z2
Vf = newton(f,0.15)
plt.annotate(r'$V_f= %1.5fV$'%(Vf),xy=(Vf,0),
         xytext=(0.2, 0.05),
         fontsize=14,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=.2",color='chocolate'),color='chocolate')
plt.plot([Vf],[0],'o',color='gold')

xp = np.linspace(-0.8, 0, 100)
#Se grafican jos ejes sobre la curva para que sea mas evidente el cruce por 0
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#Se grafica la dispresion de puntos de los datos junto
#con la interpolacion
plt.title('Filtro Amarillo', fontsize=20, color='gold')
plt.axis([-1.2,0.7, -1.4,0.5])
plt.plot(xp, p(xp), '-',color='gold')
plt.plot(x,y,'.',color='gold')
plt.xlabel(r'$Voltaje [V]$', fontsize=8)
plt.ylabel(r'$Corriente [A]$', fontsize=8)
plt.show()





