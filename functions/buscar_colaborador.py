def buscar_colaboradores(temas: list) -> None:
    entrada = input("Ingrese el nombre del colaborador: ").strip().lower() 

    encontrados = False
    resultados = []

    for tema in temas:
        claves = tema.keys()
        colaboradores_existe = False
        titulo_existe = False

        for clave in claves:
            if clave == "Colaboradores":
                colaboradores_existe = True
            if clave == "Título":
                titulo_existe = True

        if colaboradores_existe and titulo_existe:
            colaboradores = tema["Colaboradores"]
            titulo = tema["Título"]

            if isinstance(colaboradores, list):
                for colaborador in colaboradores:
                    if entrada == colaborador.strip().lower():
                        print("Título:", titulo)
                        resultados.append([entrada, titulo])
                        encontrados = True
                        break 

    if encontrados == False:
        print("No se encontraron temas con ese colaborador.")
    else:
        archivo = open("colaboradores.csv", "a")
        archivo.write("Colaborador,Título\n") 

        for fila in resultados:
            colaborador = fila[0]
            titulo = fila[1]
            archivo.write(f"{colaborador},{titulo}\n") 

        archivo.close()
        print("Los resultados fueron guardados en 'colaboradores.csv'")
