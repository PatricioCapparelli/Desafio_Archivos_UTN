
def buscar_colaboradores(temas: list) -> None:
    entrada = input("Ingrese el nombre del colaborador: ").strip()
    
    nombre = ""
    for letra in entrada:
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            nombre += chr(codigo + 32)
        else:
            nombre += letra

    encontrados = False
    resultados = []  #csv

    for tema in temas:
        claves = list(tema.keys())
        tiene_colab = False
        tiene_titulo = False

        for k in claves:
            if k == "Colaboradores":
                tiene_colab = True
                clave_colab = k
            elif k == "Título":
                tiene_titulo = True
                clave_titulo = k

        if tiene_colab and tiene_titulo:
            colaboradores = tema[clave_colab]
            titulo = tema[clave_titulo]

            if type(colaboradores) == list:
                for colab in colaboradores:
                    comparado = ""
                    for letra in colab:
                        codigo = ord(letra)
                        if 65 <= codigo <= 90:
                            comparado += chr(codigo + 32)
                        else:
                            comparado += letra

                    if len(nombre) == len(comparado):
                        iguales = True
                        for i in range(len(nombre)):
                            if nombre[i] != comparado[i]:
                                iguales = False
                                break
                        if iguales:
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
