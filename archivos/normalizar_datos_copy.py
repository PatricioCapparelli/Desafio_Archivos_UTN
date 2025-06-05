from archivos.individuales import *

def normalizar_datos(playlist: list) -> list:
    matriz = []
    for video in playlist:
        campo_colab_titulo = video[0]
        video_normalizado = {
            "Título": normalizar_titulo(campo_colab_titulo),
            "Colaboradores": normalizar_colaboradores(campo_colab_titulo),
            "Vistas": normalizar_vistas(video[2]),
            "Duración": normalizar_duracion(video[3]),
            "Link": normalizar_link(video[4]),
            "Fecha de lanzamiento": normalizar_fecha(video[5])
        }
        matriz.append(video_normalizado)
        
    print(matriz)
    return matriz
