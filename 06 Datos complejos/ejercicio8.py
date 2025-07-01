# Ejercicio 8
# Diccionario productos y stock con opciones de consulta, suma y agregado

productos = {
    "manzanas": 10,
    "naranjas": 15,
    "peras": 5
}

while True:
    accion = input("Ingrese acción (consultar, agregar, salir): ").lower()

    if accion == "salir":
        break

    elif accion == "consultar":
        prod = input("Producto a consultar: ").lower()
        if prod in productos:
            print(f"Stock de {prod}: {productos[prod]}")
        else:
            print(f"{prod} no existe en el stock.")

    elif accion == "agregar":
        prod = input("Producto a agregar o modificar: ").lower()
        try:
            cant = int(input("Cantidad a agregar: "))
        except ValueError:
            print("Cantidad inválida.")
            continue

        if prod in productos:
            productos[prod] += cant
        else:
            productos[prod] = cant
        print(f"Stock actualizado: {prod} = {productos[prod]}")

    else:
        print("Acción no válida.")
