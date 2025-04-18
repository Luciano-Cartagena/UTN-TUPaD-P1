#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

# Pedimos al usuario que ingrese una frase o palabra
# luego tomamos la última letra con [-1] y la pasamos a minúscula con lower()
frase = (input("Ingrese una frase o palabra: "))
ultima_letra = frase[-1].lower()

# Verificamos si la última letra es una vocal
if ultima_letra in "aeiou":
    # Si termina en vocal, se le agrega un signo de exclamación al final
    print (frase+"!")
else:
    # Si no termina en vocal, se muestra la frase tal como fue ingresada
    print(frase)