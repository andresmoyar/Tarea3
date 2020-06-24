# Tarea3 Modelos probabilísticos de señales y sistemas 
# Andrés Moya Ramírez B54889
Es mi código fuente de la tarea 3 de modelos probabilísticos. Se encuentra el código fuente y las gráficas obtenidas. 
# Parte 1-Mejor Curva de ajuste para las funciones de densidad marginales de X y Y
Para esta parte se tiene que leer el .csv y se divide en dos arreglos, uno con las sumatorias de los datos marginales de x y otro con los datos marginales de y. Luegos se usa linspace para generar los valores de 5 hasta 15 en ¨x¨ y 5 hasta 25 en ¨y¨

# Parte 1 Mejor Curva de ajuste

"source": [

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
]
