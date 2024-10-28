from pablo.parte_1 import personajes

# Diccionario para almacenar el equipamiento
equipos = {}

# Función para añadir un equipamiento
def crear_equipamiento():
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
def equipar_objeto():
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

crear_equipamiento()
equipar_objeto()
