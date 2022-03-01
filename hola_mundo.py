import matplotlib.pyplot as plt
import numpy as np
import time

# crear entorno
#py -3 -m venv .venv
#.venv\scripts\activate
#
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#python -m pip install matplotlib
"""
palabra = "Ryky"
palabra2 = "Maru"
palabra3 = palabra+" "+palabra2

#print(len(palabra3))

inicio = [1,2,3,4,5,6]
cuadrados = []

i=0
 
while i<len(inicio):
    #print(cuadrados[i]  ** 2)
    cuadrados.append( inicio[i] ** 2)
    i = i+1


#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(inicio, cuadrados)       # Plot the sine of each x point
plt.show()                   # Display the plot

"""
"""
# adivinar numero de numeros aleatorios generados
# 0:10 array size 10
control = 1

print("Para salir digite s")
while control:
    numeros_aleatorios = np.random.randint(10, size=(10))    
    x = int(input("Ingrese un número: "))
    repeticiones = np.where(numeros_aleatorios == x)[0]
    if len(repeticiones) > 0:
        print("número de repeticiones es: ")
        print(len(repeticiones))
        print(numeros_aleatorios)
    elif len(repeticiones) == 0:
        print("No exixten coincidencias")
        print(numeros_aleatorios)
    else:
        print("Debe ingresar un número valido")
"""
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
"""    
"""
start = time.time()

arreglo_aleatorio = np.random.randint(10, size=(10))
print(arreglo_aleatorio)
print("-frecuencias-")

(unique, counts) = np.unique(arreglo_aleatorio, return_counts=True)

frequencies = np.asarray((unique, counts)).T
print(frequencies)

end = time.time()
print("tiempo de ejecución: ",end - start," seg")
"""
lista_elementos = []
lista_resultado = []

def buscar(elemento, lista):
    try:
        item = lista.index(elemento)
        return item
    except ValueError:
        return -1        

list_aleatoria = np.random.randint(10, size=(10)).tolist()

for numero in list_aleatoria:
    item_inicial = buscar(numero, lista_elementos)    
    if item_inicial == -1:
        coincidencias = list_aleatoria.count(numero)        
        lista_elementos.append(numero)
        tupla_tmp = [numero,coincidencias]
        lista_resultado.append(tupla_tmp)
        
print(list_aleatoria)
print("-----")        
print(lista_resultado)
