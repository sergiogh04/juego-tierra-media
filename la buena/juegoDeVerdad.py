

def  añadir_equipamiento():
    return print("")

def  equipar_arma():
    return print("")


def  relaciones_personajes():
    return print("")

def mover_personaje():
    return print("")

def simular_batalla():
    return print("")

def personajes_faccion():
    return print("")

def buscar_personajes():
    return print("")

def mostrar_personajes():
    return print("")



def menu_juego():
    personajes = {}
    equipos = {}
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))

        match opcion:
            case 1:
                registrar_personaje(personajes)
                print("\n")
            case 2:
                crear_equipamiento(equipos)
                print("\n")
            case 3:
                equipar_objeto(personajes,equipos)
                print("\n")
            case 4:
                relaciones_personajes(personajes)
                print("\n")
            case 5:
                ubicacion_personaje(personajes)
                print("\n")
            case 6:
                simular_batalla()
                print("\n")
            case 7:
                personajes_faccion()
                print("\n")
            case 8:
                buscar_personajes()
                print("\n")
            case 9:
                mostrar_personajes()
                print("\n")
            case 10:
                print("Has salido del programa")
                break
            case _:
                print("Opción no valida")


def mostrar_menu():
    print("""--- Menú de Gestión de la Tierra Media ---
    1. Registrar un nuevo personaje
    2. Añadir equipamiento a un personaje
    3. Equipar un arma a un personaje
    4. Establecer relaciones entre personajes
    5. Mover un personaje a una nueva localización
    6. Simular una batalla entre dos personajes
    7. Listar personajes por facción
    8. Buscar personajes por equipamiento
    9. Mostrar todos los personajes
    10. Salir""")


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




# Función para añadir un equipamiento
def crear_equipamiento(equipos):
    print("---------- CREAR EQUIPAMIENTO -------------")
    nombre = input("Introduzca el nombre del objeto: ")

    if nombre in equipos:
        print(f"Ya existe un equipo con el nombre '{nombre}'")
        return

    tipo = input("Introduce el tipo de equipo (Arma, Armadura, Objeto especial): ")

    while True:
        try:
            potencia = int(input("Introduce la potencia del equipo (debe ser un número positivo): "))
            if potencia > 0:
                break
            else:
                print("La potencia tiene que ser positiva")
        except ValueError:
            print("ERROR, el número no es válido")

    equipo = {
        "Nombre": nombre,
        "Tipo": tipo,
        "Potencia": potencia,
    }

    equipos[nombre] = equipo
    print(f"Se ha añadido '{equipo['Nombre']}' al arsenal")
    print("Estos son sus datos: ")

    for key, value in equipo.items():
        print(f"{key}: {value}")




# Función para equipar el objeto
def equipar_objeto(personajes,equipos):
    print("---------- EQUIPAMIENTO -------------")
    nombre_personaje = input("Introduzca el nombre del personaje que quieres equipar: ")

    if nombre_personaje in personajes:
        personaje = personajes[nombre_personaje]
        print(f"Se ha encontrado al personaje llamado {nombre_personaje}")

        print("Este es el equipamiento que se puede añadir: ")
        for nombre, equipo in equipos.items():
            print(f"Nombre: {equipo['Nombre']}, Tipo: {equipo['Tipo']}, Potencia: {equipo['Potencia']}")

        equipo_personaje = input("Escribe el nombre del equipo que quieres darle al personaje: ")

        if equipo_personaje in equipos:
            personaje['equipamiento'].append(equipos[equipo_personaje])
            print(f"Se ha añadido '{equipo_personaje}' a {nombre_personaje}.")
            print(f"Equipamiento actual de {nombre_personaje}: {personaje['equipamiento']}")
        else:
            print(f"El equipamiento '{equipo_personaje}' no existe")
    else:
        print(f"El personaje '{nombre_personaje}' no existe")


def relaciones_personajes(personajes):

    while True:
        pj1 = input("Introduce el nombre del primer personaje: ").strip()
        pj2 = input("Introduce el nombre del segundo personaje: ").strip()

        if pj1 in personajes and pj2 in personajes:
            break  # Salir del bucle si ambos personajes están registrados
        else:
            print("Uno o ambos personajes no están registrados. Por favor, vuelve a intentarlo.")


    tipo_relacion = ["amigos", "enemigos", "neutrales"]
    relacion_personajes = input(
        "¿Qué tipo de relación tienen los personajes? (amigos, enemigos, neutrales): ").lower().strip()

    if relacion_personajes in tipo_relacion:
        # Almacenar la relación
        personajes[pj1]["relaciones"].append({
            "personaje_relacionado": pj2,
            "tipo_relacion": relacion_personajes,
        })

        personajes[pj2]["relaciones"].append({
            "personaje_relacionado": pj1,
            "tipo_relacion": relacion_personajes,
        })

        print(f"Relación establecida: {pj1} y {pj2} son {relacion_personajes}.")

        while True:
            try:
                nivel_confianza = int(input(f"¿Qué nivel de confianza tiene {pj1} con {pj2}? (Elige del 1 al 10): "))
                if 1 <= nivel_confianza <= 10:
                    # Almacenar el nivel de confianza en las relaciones
                    personajes[pj1]["relaciones"][-1]["nivel_confianza"] = nivel_confianza
                    personajes[pj2]["relaciones"][-1]["nivel_confianza"] = nivel_confianza
                    print(f"El nivel de confianza es de {nivel_confianza}.")
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 10.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")
    else:
        print("Tipo de relación no válido. Elige entre: amigos, enemigos, neutrales.")
        return pj1, pj2, None, None

    # Devolver información de la relación y el nivel de confianza
    return pj1, pj2, relacion_personajes, nivel_confianza

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



#No se toca
if __name__ == "__main__":
    menu_juego()