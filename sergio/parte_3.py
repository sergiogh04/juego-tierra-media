


def relaciones_personajes(personajes):
    pj1 = input("Introduce el nombre del primer personaje: ").strip()
    pj2 = input("Introduce el nombre del segundo personaje: ").strip()

    tipo_relacion = ["amigos", "enemigos", "neutrales"]

    relacion_personajes = input("¿Qué tipo de relación tienen los personajes? (amigos, enemigos, neutrales): ").lower().strip()

    if relacion_personajes in tipo_relacion:
        if pj1 not in personajes:
            personajes[pj1] = {"relaciones": []}
        if pj2 not in personajes:
            personajes[pj2] = {"relaciones": []}

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
                    print(f"El nivel de confianza es de {nivel_confianza}.")
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 10.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")
    else:
        print("Tipo de relación no válido. Elige entre: amigos, enemigos, neutrales.")
        # Si la relación es inválida, establecemos valores predeterminados
        return pj1, pj2, None, None

    # Devolver información de la relación y el nivel de confianza
    return pj1, pj2, relacion_personajes, nivel_confianza

personajes = {}
pj1, pj2, relacion_personaje, nivel_confianza = relaciones_personajes(personajes)

if relacion_personaje is not None and nivel_confianza is not None:
    print(f"{pj1} y {pj2} son {relacion_personaje} y tienen una confianza de {nivel_confianza}.")
