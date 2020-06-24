# Tarea3 
## IE0405-Modelos probabilísticos de señales y sistemas 
## Andrés Moya Ramírez B54889
Es mi código fuente de la tarea 3 de modelos probabilísticos. Se encuentra el código fuente y las gráficas obtenidas. 
## Parte 1-Mejor Curva de ajuste para las funciones de densidad marginales de X y Y
Para esta parte se tiene que leer el .csv y se divide en dos arreglos, uno con las sumatorias de los datos marginales de x y otro con los datos marginales de y. Luegos se usa linspace para generar los valores de 5 hasta 15 en ¨x¨ y 5 hasta 25 en ¨y¨. Luego se aplica la sumatoria para densidades marginales con la función de numpy de sumar partes de la matriz obtenida. Luego se aplica la ecuación de densidad de Gauss para determinar sus párametros como se muestra en el código a continuación. En la parte 4 se colocan todas las gráficas, en ellas se encuentra la forma de solo las curvas con el ruido, que da la forma de Gauss.Las librerías para hacer el código son las siguientes:
```python
#Tarea3-Modelos Andrés Moya R. B54889
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit
```


### Código usado para obtener los parámetros de la mejor curva de ajuste
```python
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
```
Lo que da un <img src="https://render.githubusercontent.com/render/math?math=\sigma"> para "x" de: 3.29944286 y para "y" de: 6.02693775

Lo que da un <img src="https://render.githubusercontent.com/render/math?math=\mu"> para "x" de: 9.90484381 y para "y" de: 15.0794609 
## Parte 2-Expresión de la función de densidad conjunta que modela los datos

Para determinar esto se sabe que fx,y(x,y)=fx(x)fy(y).

Se tiene que ambos son funciones de Gauss, para ello se tiene multiplicar ambas funciones para obtener la función de densidad conjunta.

A continuación se coloca el procedimiento y su resultado.

<img src="https://render.githubusercontent.com/render/math?math=f(x)=ae^{-(x-\mu)^{2}/2\sigma^{2}}">

Es lo mismo para ambas, solo cambia el <img src="https://render.githubusercontent.com/render/math?math=\mu"> , el <img src="https://render.githubusercontent.com/render/math?math=\sigma"> y el a (punto más alto). Cuando se multplican queda:

<img src="https://render.githubusercontent.com/render/math?math=fx,y(x,y)=(ab)e^{-(x-\9.90484381)^{2}/2*3.29944286^{2}-(y-15.0794609)^{2}/2*6.02693775^{2}}">

Siendo a y b los puntos más altos de "x" y "y" respectivamente. Se suman los exponentes.

## Parte 3-Expresión de la función de densidad conjunta que modela los datos
### La correlación
Es el grado en el cual dos o más cantidades están linealmente asociadas. Para hacer esto se tiene que en cantidades discretas es la sumatoria de la función de densidad, multiplicada por las variables de "x" y "y", estos son los términos que varía la sumatoria(fxy,x,y).

<img src="https://render.githubusercontent.com/render/math?math=Rxy=\Sigma%20\Sigma%20xyf_{xy}(x,y)">

Se hace usa los datos que contienen la probabilidad y luego se hace que se hace la sumatoria con el ciclo for y la multiplicación de ambos
#### El código usado para encontrar la correlación es el siguiente:
```python

#Parte3

dfp = pd.read_csv("xyp.csv",header = 0)
x1 = dfp["x"] 
y1 = dfp["y"] 
p = dfp["p"]
correlacion=0
for i in range(len(dfp)):
  correlacion = correlacion + x1[i]*y1[i]*p[i]; 
print( "Correlacion :" ,correlacion)

```
La correlación encontrada es la siguiente:

Correlación: 149.54281000000012
### La Covarianza
Indica el grado de variación de variación de dos variables aleatorias respecto a su medida. En la fórmula se hace la resta de la correlación y la media. Al ser una función de Gauss, se obtiene que la media es el <img src="https://render.githubusercontent.com/render/math?math=\mu">, por ello se usan las de cada uno, para "x" y "y".


```python
covarianza = correlacion - (param[0]*paramy[0])
print( "Covarianza :" ,covarianza)

```
Para los datos utilizados da lo siguiente:

Covarianza: 0.18310501696706183
### El coeficiente de Correlación
El coeficiente de correlación de Pearson es lo que determina la dependencia de dos variables aleatorias. Esto se obtiene al dividir la covarianza entre la desviación estándar de "x" y "y". Alplicando esto para Gauss, da el siguiente código.

```python
cc = covarianza/ (param[1]*paramy[1]*4)
print( "Coeficiente de correlación:" ,cc)

```
El valor deber encontrarse entre -1 y 1. El valor siguiente se encuentra dentro de ese rango.

Coeficiente de correlación: 0.002301987358892183

## Parte 4-Gráficas en 2D y 3D

Con lo encontrado anteriormente y el siguiente código se generan las gráficas del modelo. 

```python
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

```
<img src="https://github.com/andresmoyar/Tarea3/blob/master/CurvaGaussianaFy.png">
