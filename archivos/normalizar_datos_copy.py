from datetime import datetime

def normalizar_datos(playlist: list) -> None:
    for video in playlist:
        video["Título"] = video["Tema"].split("|")[0].strip() if "|" in video["Tema"] else video["Tema"]
        
        video["Colaboradores"] = video.get("Colaboradores", [])
        
        vistas_str = video["Vistas"].split()[0]
        video["Vistas"] = int(float(vistas_str) * 1000000) if "millones" in video["Vistas"] else int(vistas_str)
        
        minutos, segundos = map(int, video["Duracion"].split(":"))
        video["Duración"] = minutos * 60 + segundos
        
        video["Link"] = video["Link Youtube"]
        
        fecha_str = video["Fecha lanzamiento"]
        video["Fecha de lanzamiento"] = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        
        campos_antiguos = ["Tema", "Duracion", "Link Youtube", "Fecha lanzamiento"]
        for campo in campos_antiguos:
            video.pop(campo, None)

