import json

def guardar_todas_las_canciones_en_json(lista_canciones, nombre_archivo="canciones.json"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_canciones, archivo, ensure_ascii=False, indent=4)
    print(f"✅ Archivo '{nombre_archivo}' creado con todas las canciones.")
