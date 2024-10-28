


def ubicacion_personaje(personajes):


    while True:
        nombre = input("Introduce el nombre del primer personaje: ").strip()


        if nombre in personajes:
            break  # Salir del bucle si ambos personajes están registrados
        else:
            print("El personaje no esta registrado no están registrados. Por favor, vuelve a intentarlo.")

    nueva_ubicacion = input("Introduce la nueva ubicación: ").strip()
    personajes[nombre]["ubicacion"] = nueva_ubicacion
    print(f"{nombre} ha sido movido a {nueva_ubicacion}.")

personajes = {
    "pablo": {
        "raza": "Humano",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Rivendel",
        "equipamiento": [
            {"nombre": "Andúril", "tipo": "Espada", "potencia": 80}
        ],
        "arma_equipada": {"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
        "relaciones": [
            {"personaje_relacionado": "Legolas", "tipo_relacion": "Amigo", "nivel_confianza": 10}
        ]
    },
    "juanma": {
        "raza": "Elfo",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Bosque Negro",
        "equipamiento": [
            {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70}
        ],
        "arma_equipada": {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70},
        "relaciones": [
            {"personaje_relacionado": "Aragorn", "tipo_relacion": "Amigo", "nivel_confianza": 10}
        ]
    }
}
ubicacion_personaje(personajes)