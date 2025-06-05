import json

def guardar_todas_las_canciones_en_json(lista_canciones, nombre_archivo):
    canciones_serializables = []
    for cancion in lista_canciones:
        if not isinstance(cancion, dict):
            continue
        copia = cancion.copy()
        if isinstance(copia.get("Fecha de lanzamiento"), (str, type(None))):
            pass  
        else:
            copia["Fecha de lanzamiento"] = copia["Fecha de lanzamiento"].isoformat()
        canciones_serializables.append(copia)

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(canciones_serializables, archivo, ensure_ascii=False, indent=4)
