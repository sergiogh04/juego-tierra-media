from PyQt5.QtCore.QUrl import password

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

def registrar_personaje():
    return print("personaje elegido")

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

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            match opcion:

                case 1:
                    registrar_personaje()

                case 2:
                     añadir_equipamiento()

                case 3:
                     equipar_arma()

                case 4:
                    relaciones_personajes()

                case 5:
                    mover_personaje()

                case 6:
                   simular_batalla()

                case 7:
                   personajes_faccion()

                case 8:
                    buscar_personajes()

                case 9:
                   mostrar_personajes()

                case 10:
                     print("Has salido del programa")
                     break

                case _:
                    print("Opción no valida")

        except ValueError:
            print("Introduce un numero valido")

