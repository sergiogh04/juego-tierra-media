
def registrar_personaje(personajes):
    print("------ REGISTRAR UN NUEVO PERSONAJE ------")
    nombre = input("Introduzca el nombre del personaje: ")
    if nombre in personajes:
        print("Personaje ya existe")
        return

    raza = input("Razas (Elfo, Humano, Enano, Hobbit): ")
    faccion = input("Facción del personaje: ")
    ubicacion = input("Ubicación del personaje: ")

    personaje = {
        "nombre": nombre,
        "raza": raza,
        "faccion": faccion,
        "ubicacion": ubicacion,
        "equipamiento": [],
        "relaciones": [],
    }

    personajes[nombre] = personaje
    print(f"Personaje '{personaje["nombre"]}' registrado exitosamente")
    print(personajes)

def listar_personajes_faccion(personajes):
    faccion = input("Introduzca el nombre de una facción: ")
    personajes_faccion = []
    for nombre, informacion in personajes.items():
        if informacion.get("faccion") == faccion:
            personajes_faccion.append(nombre)

    if personajes_faccion:
        print(f"Personajes en la facción '{faccion}':")
        print(personajes_faccion)
    else:
        print(f"No se encontraron personajes en la facción '{faccion}'.")



personajes = {
    "Aragorn": {
        "raza": "Humano",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Rivendel",
        "equipamiento": [
            {"nombre": "Andúril", "tipo": "Espada", "potencia": 80}
        ],
        "arma_equipada": {"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
        "relaciones": [
            {"personaje": "Legolas", "tipo": "Amigo", "nivel_confianza": 10}
        ]
    },
    "Legolas": {
        "raza": "Elfo",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Bosque Negro",
        "equipamiento": [
            {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70}
        ],
        "arma_equipada": {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70},
        "relaciones": [
            {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 10}
        ]
    }
}

listar_personajes_faccion(personajes)

