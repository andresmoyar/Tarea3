# Tarea3 
## IE0405-Modelos probabilísticos de señales y sistemas 
## Andrés Moya Ramírez B54889
Es mi código fuente de la tarea 3 de modelos probabilísticos. Se encuentra el código fuente y las gráficas obtenidas. 
## Parte 1-Mejor Curva de ajuste para las funciones de densidad marginales de X y Y
Para esta parte se tiene que leer el .csv y se divide en dos arreglos, uno con las sumatorias de los datos marginales de x y otro con los datos marginales de y. Luegos se usa linspace para generar los valores de 5 hasta 15 en ¨x¨ y 5 hasta 25 en ¨y¨. Luego se aplica la sumatoria para densidades marginales con la función de numpy de sumar partes de la matriz obtenida. Luego se aplica la ecuación de densidad de Gauss para determinar sus párametros como se muestra en el código a continuación. En la parte 4 se colocan todas las gráficas, en ellas se encuentra la forma de solo las curvas con el ruido, que da la forma de Gauss.

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
Correlación: 149.54281000000012
Covarianza: 149.54281000000012
Coeficiente de variación: 0.002301987358892183

