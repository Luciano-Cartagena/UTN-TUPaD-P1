# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Definimos la función celsius_a_fahrenheit que recibe una temperatura en grados Celsius
def celsius_a_fahrenheit(celsius):
    # Calculamos la temperatura en Fahrenheit usando la fórmula (C * 9/5) + 32
    return (celsius * 9 / 5) + 32

# Solicitamos al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en Celsius: "))

# Llamamos a la función para convertir la temperatura a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostramos el resultado de la conversión por pantalla
print(f"La temperatura equivalente de Celsius {celsius} a Fahrenheit es: {fahrenheit}")
