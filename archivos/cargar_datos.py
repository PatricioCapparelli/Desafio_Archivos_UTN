from archivos.cargar_csv import guardar_y_mostrar_datos_csv
from archivos.normalizar_datos_copy import normalizar_datos

def cargar_normalizar_y_guardar_datos() -> list:
    # Cargo las canciones desde CSV
    canciones = guardar_y_mostrar_datos_csv()
    # Normalizo los datos
    temas = normalizar_datos(canciones)
    return temas

