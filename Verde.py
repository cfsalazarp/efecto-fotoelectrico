#Integrantes:
#Luisa Fernanda Torregrosa Serrato - 20152005054
#Daniel Valencia Gómez - 20161005027
#Christian Salazar Piñeros - 20161005082

# EXPERIMENTO EFECTO FOTOELECTRICO (VERDE) #

#Se importa las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

fig,ax = plt.subplots(figsize=(16,9))
fig.canvas.set_window_title('Experimento Filtro Verde')  

#Se ingresan los datos de voltaje (x) y corriente (y) obtenidos
#experimentalmente en el laboratorio
x = np.array([-0.05,-0.1,-0.18,-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8])
y = np.array([0.6,0.2,0.0,-0.2,-0.5,-0.8,-1.1,-1.3,-1.5,-1.7])

#Se realiza un ajuste polinomial de grado 2
z = np.polyfit(x, y, 2)
p = np.poly1d(z)

#Se ajusta el vector arrojado en z para cuadrar el polinomio
z4=z[0]
z3=z[1]
z2=z[2]
#Se obtiene el polinomio de ajuste
plt.text(-1.2,-0.5, 'El polinomio de ajuste es:', fontsize = 10)
plt.text(-1.2,-0.7, r'$%0.3fx^2+%0.3fx+%0.3f$'
         %(z4,z3,z2),fontsize=13)

#Se resuelve el polinomio para hallar el voltaje de frenado
def f(x):
    return (z4*x**2)+(z3*x)+z2
Vf = newton(f,0.15)
plt.annotate(r'$V_f= %1.5fV$'%(Vf),xy=(Vf,0),
         xytext=(-0.6, 0.6),
         fontsize=14,
         arrowprops=dict(arrowstyle="->",
         connectionstyle="arc3,rad=-.2",color='chocolate'),color='chocolate')
plt.plot([Vf],[0],'o',color='green')

xp = np.linspace(-0.9, 0, 100)
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
plt.title('Filtro Verde', fontsize=20, color='green')
plt.axis([-1.2,0.2, -2,1])
plt.plot(xp, p(xp), '-',color='green')
plt.plot(x,y,'.',color='green')
plt.xlabel(r'$Voltaje [V]$', fontsize=8)
plt.ylabel(r'$Corriente [A]$', fontsize=8)
plt.show()