def codigo_en_link(codigo: str, link: str) -> bool:
    len_codigo = len(codigo)
    len_link = len(link)
    resultado = False
    for i in range(len_link - len_codigo + 1):
        coincide = True
        for j in range(len_codigo):
            if link[i + j] != codigo[j]:
                coincide = False
                break
        if coincide:
            resultado = True
            break
    return resultado

def buscar_video_por_codigo(temas: list) -> None:
    codigo_ingresado = input(f"Ingrese el codigo del video (lo que sigue despues de 'v='): \n")
    encontrado = False
    for tema in temas:
        link = tema["Link"]
        if codigo_en_link(codigo_ingresado, link):
            for clave in tema:
                print(f"{clave}: {tema[clave]}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontro video con codigo: {codigo_ingresado}")
