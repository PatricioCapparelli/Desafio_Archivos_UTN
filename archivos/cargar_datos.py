from archivos.cargar_csv import guardar_y_mostrar_datos_csv
from archivos.guardar_en_json import guardar_todas_las_canciones_en_json
from archivos.normalizar_datos_copy import normalizar_datos

def cargar_normalizar_y_guardar_datos() -> list:
    todos_los_temas = "canciones.json"

    # Cargo las canciones desde CSV
    canciones = guardar_y_mostrar_datos_csv()

    # Normalizo los datos
    temas = normalizar_datos(canciones)

    # Guardo en JSON
    guardar_todas_las_canciones_en_json(canciones, todos_los_temas)

    return temas

