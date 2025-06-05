def mostrar_temas(temas: list) -> None:
    print(f"\n{'Titulo':<41} {'Duracion':>14}")
    print("-" * 55)
    
    for tema in temas:
        titulo = "Desconocido"
        duracion = 0
        
        for clave in tema:
            if clave == "Título":
                titulo = tema[clave]
        
        for clave in tema:
            if clave == "Duración":
                duracion = tema[clave]

        print(f"{titulo:<41} {duracion:>14}")
