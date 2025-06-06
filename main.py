from archivos.cargar_datos import cargar_normalizar_y_guardar_datos
from archivos.guardar_en_json import guardar_todas_las_canciones_en_json
from functions.mostrar_temas import mostrar_temas
from functions.mostrar_temas import mostrar_temas
from functions.ordenar_temas_por_duracion import ordenar_temas_por_duracion
from functions.calcular_promedio_de_visitas import promedio_vistas
from functions.maxima_minima import videos_maximas_vistas,videos_minimas_vistas
from functions.buscar_por_codigo import buscar_video_por_codigo
from functions.buscar_colaborador import buscar_colaboradores
from functions.buscar_por_mes import buscar_por_mes
from validaciones.menu_copy import menu

datos_cargados = False
promedios = None
mensaje_error = "\nError: Primero debe normalizar los datos, ingrese la opcion 1."

while True:
    opcion = menu("\nMENU PRINCIPAL\n1 - Normalizar datos.\n2 - Mostrar todos los temas.\n3 - Ordenar temas.\n4 - Calcular promedio de vistas.\n5 - Ver video con mayor cantidad de vistas.\n6 - Ver video con menor cantidad de vistas.\n7 - Buscar por codigo.\n8 - Buscar tema por colaborador.\n9 - Ver por mes de lanzamiento.\n10 - Guardar en JSON.\n11 - Salir.")

    match opcion:
        case 1:
            temas = cargar_normalizar_y_guardar_datos()
            datos_cargados = True
        case 2:
            if datos_cargados:
                mostrar_temas(temas)
            else:
                print(mensaje_error)
        case 3:
            if datos_cargados:
                ordenar_temas_por_duracion(temas)
            else:
                print(mensaje_error)
        case 4:
            if datos_cargados:
                promedio_vistas(temas)
            else:
                print(mensaje_error)
        case 5:
            if datos_cargados:
                videos_maximas_vistas(temas)
            else:
                print(mensaje_error)
        case 6:
            if datos_cargados:
                videos_minimas_vistas(temas)
            else:
                print(mensaje_error)
        case 7:
            if datos_cargados:
                buscar_video_por_codigo(temas)
            else:
                print(mensaje_error)
        case 8:
            if datos_cargados:
                buscar_colaboradores(temas)
            else:
                print(mensaje_error)
        case 9:
            if datos_cargados:
                buscar_por_mes(temas)
            else:
                print(mensaje_error)
        case 10:
            if datos_cargados:
                guardar_todas_las_canciones_en_json(temas)
            else:
                print(mensaje_error)
        case 11:
            break
        case _:
            print("Opcion invalida. Intente nuevamente.")