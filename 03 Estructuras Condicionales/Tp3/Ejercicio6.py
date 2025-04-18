#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

# Genera una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostramos los resultados
print ("Numero Aleatorios: ", numeros_aleatorios)
print ("Media: ", media)
print ("Mediana: ",mediana)
print ("Moda: ", moda)

# Análisis del sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o la izquierda.")
else:
    print("Sin Sesgo.")


