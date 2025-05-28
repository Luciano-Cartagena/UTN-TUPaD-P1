#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 

# Se crea una lista de números desde el 10 hasta el 30 inclusive, en saltos de 5 en 5.
# Es decir: [10, 15, 20, 25, 30]
numeros = list(range(10, 31, 5))

# Se imprime una sublista con los dos primeros elementos usando slicing.
# numeros[:2] toma los elementos en las posiciones 0 y 1.
print(numeros[:2])
