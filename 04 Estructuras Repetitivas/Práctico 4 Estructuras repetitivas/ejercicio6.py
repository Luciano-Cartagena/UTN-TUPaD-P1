#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

# Usamos un bucle for con range() para recorrer los números desde 100 hasta 0 (inclusive), bajando de 2 en 2
for i in range(100, -1, -2):  
    # Imprimimos cada número i (que será par, porque empezamos en 100 y restamos de a 2)
    print(i)
