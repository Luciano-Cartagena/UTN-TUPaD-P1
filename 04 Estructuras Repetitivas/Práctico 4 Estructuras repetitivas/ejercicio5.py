#) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  # Importamos el módulo random para generar números aleatorios

# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializamos el contador de intentos en 0
intentos = 0

# Usamos una bandera (adivinado) para controlar el bucle while
adivinado = False

# Bucle que se repite hasta que adivinen el número
while not adivinado:
    # Pedimos al usuario que ingrese un número entre 0 y 9
    numero_usuario = int(input("Ingresa un número entre 0 y 9: "))
    
    # Sumamos 1 al contador de intentos
    intentos += 1

    # Verificamos si el número ingresado es igual al número aleatorio
    if numero_usuario == numero_aleatorio:
        # Si lo adivinó, cambiamos la bandera para salir del bucle
        adivinado = True
    else:
        # Si no lo adivinó, le avisamos que intente de nuevo
        print("No es el número, intenta de nuevo.")

# Cuando sale del bucle, mostramos el mensaje de éxito con el número y la cantidad de intentos
print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
