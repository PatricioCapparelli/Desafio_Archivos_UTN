def menu(texto_menu: str) -> int:
    '''Muestra el menu y valida la opcion ingresada (1 a 11).'''
    print(texto_menu)
    opcion = input("Seleccione opcion: ")
    numero = 0

    while True:
        if opcion.isdigit(): 
            opcion_int = int(opcion)
            numero = opcion_int
            break
        else:
            opcion = input("Error: Seleccione opcion valida (1-11): ")

    return numero