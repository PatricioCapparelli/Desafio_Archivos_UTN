from functions.mostrar_temas import mostrar_temas

def ordenar_temas_por_duracion(temas: list) -> None:
    duracion = clave_duracion
    orden = sorted(temas, key=duracion, reverse=True)
    mostrar_temas(orden)
    return orden

def clave_duracion(tema: dict) -> int:
        duracion = 0

        for clave in tema:
            if clave == "Duración":
                duracion = tema[clave]

        return duracion
