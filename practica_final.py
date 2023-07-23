'''Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. El programa deberá imprimir
la matriz generada y luego calcular la suma de los elementos de cada fila y
columna. Finalmente, deberá imprimir la suma de cada fila y columna.'''

import random

#Pedimos al usuario que ingrese por teclado el tamaño de la matriz
N=int(input("Por favor ingrese el tamaño de la matriz:  "))

def num_valido (N):
   try:
      

#Creamos una matriz vacia
matriz=[]

#Usamos un for para crear las filas
for i in range (N):
    #Creamos una fila vacia
    fila= []
    #Hacemos otro for para crear las columnas
    for j in range(N):
        #Introducimos los números aleatorios a la fila
        fila.append(random.randint(0,9))
    #Añadimos los datos a la matriz    
    matriz.append(fila)


#Creamos una función para imprimir la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
     print(fila)

#Imprimimos las matriz, llamando a la función
mostrar_matriz(matriz)

#Calcular la suma de cada fila y columna.
#Calculamos la cantidad de elementos que hay en la matriz, numero de filas y numero de columnas
filas=len(matriz)
columnas=len(matriz[0])


#Calculamos la suma de cada fila de la matriz
for i in range(filas):
    suma=sum(matriz[i])
    #Añadimos la suma a la matriz para que la muestre
    matriz[i].append(suma)
#Hacemos un salto de línea para que no se vea muy junto
print()

#Mostramos la matriz con la suma de las filas 
mostrar_matriz(matriz)

#Hacemos un salto de línea para que no se vea muy junto
print()

#Para guardar la suma para luego añadirla a la matriz
sum_columnas=[]

for j in range(columnas):
   #Usamos una lista para sumar por columnas
   suma=sum([fila[j]  for fila in matriz])
   sum_columnas.append(suma)



#Añadimos la suma de las columnas a la matriz
matriz.append(sum_columnas)

#Mostramos la matriz
mostrar_matriz(matriz)


