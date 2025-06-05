def guardar_canciones_por_colaborador_diccionario(lista_diccionarios, colaborador_buscado):
    with open("colaboradores.csv", "w", encoding="utf-8") as archivo:

        encabezados = list(lista_diccionarios[0].keys())
        archivo.write(",".join(encabezados) + "\n")

        for cancion in lista_diccionarios:
            if colaborador_buscado.lower() in str(cancion.get("Colaborador", "")).lower():
                fila = [str(cancion[key]) for key in encabezados]
                archivo.write(",".join(fila) + "\n")

    print(f"✅ Archivo 'colaboradores.csv' creado con canciones que incluyen a '{colaborador_buscado}'.")
