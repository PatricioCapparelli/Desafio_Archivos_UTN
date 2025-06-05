def clave_vistas(tema:dict) -> int:
    clave = tema["Vistas"]
    return clave

def videos_maximas_vistas(temas:list) -> None:
    vistas = clave_vistas
    temas_ordenados = sorted(temas, key=vistas, reverse=True)
    max_vistas = temas_ordenados[0]["Vistas"]

    print(f"\nVideo con maxima cantidad de vistas ({max_vistas}):")
    for tema in temas_ordenados:
        if tema["Vistas"] == max_vistas:
            print(f" - {tema['Título']}")
        else:
            break

def videos_minimas_vistas(temas:list) -> None:
    vistas = clave_vistas
    temas_ordenados = sorted(temas, key=vistas)
    min_vistas = temas_ordenados[0]["Vistas"]

    print(f"\nVideo con minima cantidad de vistas ({min_vistas}):")
    for tema in temas_ordenados:
        if tema["Vistas"] == min_vistas:
            print(f" - {tema['Título']}")
        else:
            break
