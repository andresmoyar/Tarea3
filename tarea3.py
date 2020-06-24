#Tarea3-Modelos Andrés Moya R. B54889
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit

#Parte 1 Mejor Curva de ajuste

x = np.linspace(5,15,11)
y = np.linspace(5,25,21)
df = pd.read_csv("xy.csv")
arr = df.to_numpy()
arr=np.delete(arr,0,1)
sumy= np.sum(arr,axis=0)
sumx= np.sum(arr,axis=1)
#Curva de mejor ajuste .Las dos figuras obtenidas eran una curva de Gauss
def gaussiana(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
param,_=curve_fit(gaussiana,x,sumx)
paramy,_=curve_fit(gaussiana,y,sumy)
print(param)
print(paramy)
#Parte 2. La funcion acumulativa es fx,y(x,y)=fx(x)fy(y)
#<img src="../master/images/dato2.png" width="150"> para GitHub, ese es para ingresar las ecuaciones desde una imagen

#Parte3

dfp = pd.read_csv("xyp.csv",header = 0)

#Correlacion
x1 = dfp["x"] 
y1 = dfp["y"] 
p = dfp["p"]
correlacion=0
for i in range(len(dfp)):
  correlacion = correlacion + x1[i]*y1[i]*p[i]; 
print( "Correlacion :" ,correlacion)


#Covarianza 
covarianza = correlacion - (param[0]*paramy[0])
print( "Covarianza :" ,covarianza)


# Coeficiente de correlación
cc = covarianza/ (param[1]*paramy[1]*4)
print( "Coeficiente de correlación:" ,cc)

#Parte 4
#Curva Fx

plt.xlabel('x')
plt.ylabel('Fx')
plt.title('Curva obtenida de datos marginales en x con ruido')
plt.plot(x,sumx)
plt.show()
#Curva Fy
plt.xlabel('y')
plt.ylabel('Fy')
plt.title('Curva obtenida de datos marginales en y con ruido')

plt.plot(y,sumy)
plt.show()

#Curva Gaussiana de valores de x
mux=param[0]
sigmax=param[1]
plt.xlabel('x')
plt.ylabel('Fx')
plt.title('Curva de mejor ajuste para datos marginales de x sin ruido')
plt.plot(x,gaussiana(x,mux,sigmax))
plt.show()
#Curva de Gauss de valores de y
muy=paramy[0]
sigmay=paramy[1]
plt.xlabel('y')
plt.ylabel('Fy')
plt.title('Curva de mejor ajuste para datos de marginales y sin ruido')
plt.plot(y,gaussiana(y,muy,sigmay))
plt.show()

#Curva 3D
eje = plt.axes(projection='3d')
X = x1
Y = y1
Z = p

eje.plot_trisurf(X, Y, Z, cmap='jet')
eje.set_xlabel('X ')
eje.set_ylabel('Y ')
eje.set_zlabel('Z ')
eje.set_title('Curva 3D')
plt.show()
