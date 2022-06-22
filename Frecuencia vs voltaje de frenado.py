#Integrantes:
#Luisa Fernanda Torregrosa Serrato - 20152005054
#Daniel Valencia Gómez - 20161005027
#Christian Salazar Piñeros - 20161005082

# FRECUENCIA V.S VOLTAJE DE FRENADO #

#Se importa la libreria numpy para usar caracterer numericos
#Se importa la libreria matplotlib para graficar
#Se importa la libreria constants para usar constantes
import numpy as np
import scipy.constants as cte
import matplotlib.pyplot as plt
from scipy.optimize import newton

fig,ax = plt.subplots(figsize=(16,9))
fig.canvas.set_window_title('Frecuencia vs Voltaje de Frenado')  

#Se ingresan los datos de voltaje de frenado (y) obtenidos 
#experimentalmente en el laboratorio y la frecuencia (x)
#dada segun la longitud de ondad dada y la ecuación:
#nu=c/lambda
lazul=4360
lverde=5460
lamarillo=5780
nub=cte.c/(lazul*0.1*cte.nano) 
nug=cte.c/(lverde*0.1*cte.nano)
nuy=cte.c/(lamarillo*0.1*cte.nano)
#Se ingresan los datos de frecuencia (x) y voltaje
#de frenado (y) obtenidos experimentalmente 
x = np.array([nuy,nug,nub])
y = np.array([0.14323,0.16854,0.76246])

#Se realiza un ajuste polinomial de grado 1
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

#Se ajusta el vector arrojado en z para cuadrar el polinomio
z1=z[0]
z0=z[1]
plt.text(0.7e+14,1, 'El polinomio de ajuste es:', fontsize = 10)
plt.text(0.7e+14,0.8, r'$(%0.3e)x %0.3f$'%(z1,z0),fontsize=12)
plt.text(3e+14,1, r'Pendiente = $\frac{h}{e}$', fontsize = 12,style='italic')
plt.text(3e+14,0.8, r'$h = %0.3e$'%(z1*cte.e),bbox=dict(facecolor='white', edgecolor='red'))
plt.text(3e+14,0.65, r'Constante de Planck',color='red', fontsize = 8,style='italic')

#Se resuelve el polinomio para hallar la frecuencia umbral
def f(x):

    return (z1*x)+z0

fu = newton(f,4.9e+14)

#Se resuelve el polinomio para hallar la funcion trabajo
def fw(y):
    trabajo = (z1*y)+z0
    return trabajo


#print(ft)
#Se grafica la dispersion de puntos de los datos junto
#con la interpolacion
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
xp = np.linspace(-0.1, 8e+14, 100)
plt.axis([0,8e+14, -2.5,1.5])
plt.plot(xp, p(xp),'black')
plt.xlabel(r'$Frecuencia $ $(\nu)$', fontsize=8)
plt.ylabel(r'$Voltaje$ $de $ $Frenado $ $(V_f)$', fontsize=8)
plt.plot(nub,0.76246,'bo',label= '$V_f$ filtro azul = {}'.format(round(y[2],4)))
plt.plot(nug,0.16854,'go',label= '$V_f$ filtro verde = {}'.format(round(y[1],4)))
plt.plot(nuy,0.14323,'o',color='gold',label= '$V_f$ filtro amarillo = {}'.format(round(y[0],4)))
plt.plot([fu],[0],'s',color='black',label=r'$\nu_{umbral}= %0.2eHz$'%(fu))
plt.plot([0],z0,'^',color='red',label=r'$\frac{\phi_W}{e}= %0.2f$'%(z0))
plt.legend(loc='lower right',fontsize=13)
plt.title(r'$\nu$'+' vs '+r'$V_f$', fontsize=16, color='darkred')
plt.show()




