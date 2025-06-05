def comparar_numero_con_ascii(caracter, length: int, primer_ascii: int = 48, ultimo_ascii: int = 57) -> bool:
    '''Devuelve True si el caracter (o número convertido a caracter) está dentro del rango especificado por parámetros.'''
    caracter = str(caracter)
    valido = False
    if len(caracter) == length:
        if ord(caracter) >= primer_ascii and ord(caracter) <= ultimo_ascii:
            valido = True
    return valido