'Escribir un programa en Python que genere una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9. '
import random

#Pedimos al usuario que ingrese por teclado el tamaño de la matriz
N=int(input("Por favor ingrese el tamaño de la matriz:  "))

#Creamos una matriz vacia
matriz=[]

#Usamos un for para crear  las filas
for i in range (N):
    #Creamos una fila vacia
    fila= []
    #Hacemos otro for para crear las columnas
    for j in range(N):
        #Introducimos los números aleatorios a la fila
        fila.append(random.randint(0,9))
    #Añadimos los datos a la matriz    
    matriz.append(fila)
#Imprimimos las matriz
for fila in matriz:
    print(fila)
