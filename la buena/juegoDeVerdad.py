

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
                añadir_equipamiento()
                print("\n")
            case 3:
                equipar_arma()
                print("\n")
            case 4:
                relaciones_personajes()
                print("\n")
            case 5:
                mover_personaje()
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

if __name__ == "__main__":
    menu_juego()