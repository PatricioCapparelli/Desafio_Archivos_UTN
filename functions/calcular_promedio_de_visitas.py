def promedio_vistas(temas: list) -> None:
    total_vistas = 0
    cantidad = 0
    
    for tema in temas:
        if "Vistas" in tema:
            total_vistas += tema["Vistas"]
            cantidad += 1
    
    if cantidad > 0:
        promedio = total_vistas / cantidad / 1_000_000  
        print(f"\nPromedio de vistas: {promedio:.2f} millones")
    else:
        print("\nNo hay datos de vistas disponibles.")
