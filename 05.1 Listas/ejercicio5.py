#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#################EXPLICACIÓN##########################
#Paso 1:Se crea una lista llamada numeros que contiene: [8, 15, 3, 22, 7].
#Paso 2:Se busca el número máximo de la lista usando: max(numeros).
#Paso 3:Se elimina ese número máximo de la lista usando: numeros.remove(). 
#Paso 4:Se imprime la lista resultante: la listsa queda [8, 15, 3, 7].

#El programa crea una lista de números, identifica cuál es el número más grande y lo elimina. 
# Finalmente, muestra la lista resultante sin ese valor máximo.