#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

# Se solicita al usuario que ingrese una contraseña entre 8 y 14 caracteres.
contraseña = (input("Ingrese una contraseña entre 8 y 14 caracteres: "))

# Se imprime la cantidad de caracteres que tiene la contraseña ingresada.
print(len(contraseña))

# Se evalúa si la longitud de la contraseña está entre 8 y 14 caracteres, inclusive.
if len (contraseña) >= 8 and len (contraseña) <= 14:
    # Si la condición se cumple, se indica que la contraseña es válida.
    print("Ha Ingresado una contraseña correcta.")
else:
    # Si no se cumple la condición, se le indica al usuario que debe cumplir con el rango.
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")