
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


# Datos de ejemplo
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

# Llamar a la función
pj1, pj2, relacion_personaje, nivel_confianza = relaciones_personajes(personajes)

if relacion_personaje is not None and nivel_confianza is not None:
    print(f"{pj1} y {pj2} son {relacion_personaje} y tienen una confianza de {nivel_confianza}.")

def ubicacion_personaje(personajes):

    nombre = input("Introduce el nombre del personaje: ").strip()

    if nombre not in personajes:
        print(f"El personaje {nombre} no existe.")
        return
    nueva_ubicacion = input("Introduce la nueva ubicación: ").strip()
    personajes[nombre]["ubicacion"] = nueva_ubicacion
    print(f"{nombre} ha sido movido a {nueva_ubicacion}.")
