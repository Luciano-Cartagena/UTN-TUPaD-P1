#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores in
#gresados

# Definimos una función llamada informacion_personal que recibe 4 parámetros:
# nombre, apellido, edad y residencia
def informacion_personal(nombre, apellido, edad, residencia):
    # La función devuelve un string formateado con los datos personales
    return f"¡Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}!"

# Programa principal:
# Solicitamos al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Solicitamos al usuario que ingrese su apellido
apellido = input("Ingrese su apellido: ")

# Solicitamos al usuario que ingrese su edad (lo convertimos a entero porque input devuelve string)
edad = int(input("Ingrese su edad: "))

# Solicitamos al usuario que ingrese su lugar de residencia
residencia = input("Ingrese su lugar de residencia: ")

# Llamamos a la función informacion_personal pasándole los datos ingresados
saludo = informacion_personal(nombre, apellido, edad, residencia)

# Imprimimos el mensaje generado por la función
print(saludo)

