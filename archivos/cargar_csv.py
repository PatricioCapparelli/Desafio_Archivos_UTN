def guardar_y_mostrar_datos_csv() -> list:
    ruta = "CSV-JSON/archivos/datos.csv"

    with open(ruta, "r", encoding="utf-8") as archivo:
        matriz = []
        nombres_columnas = archivo.readline().strip().split(",")

        for linea in archivo:
            linea = linea.strip()
            valores = linea.split(",")
            fila = []

            for valor in valores:
                fila.append(int(valor) if valor.isdigit() else valor)

            matriz.append(fila)

    print(nombres_columnas)
    for fila in matriz:
        print(fila)

    return matriz
