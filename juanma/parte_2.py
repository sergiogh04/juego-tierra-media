# Diccionario para almacenar el equipamiento de los personajes
equipos = {}

# Función para añadir un equipamiento
def añadir_equipamiento():
    print("----------AÑADIR EQUIPAMIENTO-------------")
    nombre = input("Introduzca el nombre del objeto: ")

    if nombre in equipos:
        print(f"Ya existe un equipo con el nombre '{nombre}'")
        return

    tipo = input("Introduce el tipo de equipo (Arma, Armadura, Objeto especial): ")

    while True:
        try:
            potencia = int(input("Introduce la potencia del equipo siendo un numero positivo: "))
            if potencia > 0:
                break
            else:
                print("La potencia tiene que ser positiva")
        except ValueError:
            print("ERROR, el numero no es valido")

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


añadir_equipamiento()

