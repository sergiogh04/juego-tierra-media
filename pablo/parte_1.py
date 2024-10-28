
def registrar_personaje():
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



personajes = {}
registrar_personaje()

