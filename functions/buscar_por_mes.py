def buscar_por_mes(lista_videos):
    mes_buscado = input("Ingrese el numero del mes (1-12): ")
    encontrados = []
    for video in lista_videos:
        fecha = video["Fecha de lanzamiento"]
        mes = fecha.split("/")[1]
        if int(mes) == int(mes_buscado):
            encontrados.append(video)
    
    if encontrados:
        for video in encontrados:
            print(f"{video['Título']} - Fecha: {video['Fecha de lanzamiento']}")
    else:
        print("No se encontraron temas para ese mes.")
