from validaciones.menu_copy import menu

mensaje_error = "\nError: Primero debe normalizar los datos. Seleccione la opcion 1 para normalizar los datos de los videos."

while True:
    opcion = menu("\nMENU PRINCIPAL\n1 - Normalizar datos.\n2 - Mostrar temas.\n3 - Ordenar Temas.\n4 - Mostrar datos ordenados por promedio del estudiante.\n5 - Mostrar materia/s con mayor promedio.\n6 - Buscar estudiante por legajo.\n7 - Mostrar calificaciones repetidas en una asignatura.\n8 - Salir del programa.")

    match opcion:
        case 1:
            normalizar_datos(playlist_lady_gaga)
        case 2:
            mostrar_temas(playlist_lady_gaga)
        case 3:
            ordenar_temas(playlist_lady_gaga)
        case 4:
            #calcular_promedio_de_vistas()
            pass
        case 5:
            #ver_video_maxima_reproduccion()
            pass
        case 6:
            #ver_video_minima_reproducion()
            pass
        case 7:
            #buscar_por_codigo()
            pass
        case 8:
            #mostrar_videos_por_colaborador()
            pass
        case 9:
            #mostrar_video_por_mes_de_lanzamiento()
            pass
        case 10:
            #print("Saliendo del programa...")
            pass
        case _:
            #print("Opcion invalida. Intente nuevamente.")
            pass