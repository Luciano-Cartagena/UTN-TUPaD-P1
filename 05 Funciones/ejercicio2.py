#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

# Definimos una función llamada saludar_usuario que recibe un parámetro 'nombre'
def saludar_usuario(nombre):
    # La función devuelve un saludo personalizado usando f-strings
    return f"¡Hola {nombre}!"

# Programa principal:
# Solicitamos al usuario que ingrese su nombre por teclado
nombre = input("Escriba su nombre: ")

# Llamamos a la función saludar_usuario pasando el nombre que ingresó el usuario
saludo = saludar_usuario(nombre)

# Imprimimos el saludo que nos devolvió la función
print(saludo)

