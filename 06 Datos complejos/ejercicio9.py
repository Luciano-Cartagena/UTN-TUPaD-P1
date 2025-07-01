# Ejercicio 9
# Agenda con claves tuplas (día, hora) y valores eventos

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de Inglés"
}

dia = input("Ingrese día: ").lower()
hora = input("Ingrese hora (HH:MM): ")

evento = agenda.get((dia, hora))

if evento:
    print(f"Evento en {dia} a las {hora}: {evento}")
else:
    print(f"No hay eventos en {dia} a las {hora}")
