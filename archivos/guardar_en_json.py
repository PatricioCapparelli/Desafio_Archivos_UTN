import json

def guardar_todas_las_canciones_en_json(lista_canciones):
    todos_los_temas = "canciones.json"
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

    with open(todos_los_temas, "w", encoding="utf-8") as archivo:
        json.dump(canciones_serializables, archivo, ensure_ascii=False, indent=4)
