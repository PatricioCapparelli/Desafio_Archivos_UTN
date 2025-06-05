def normalizar_titulo(campo: str) -> str:
    campo = campo.strip('"').strip()
    partes = campo.split("-")
    titulo = ""
    for i in range(len(partes)):
        if i == 1:
            titulo = partes[i].strip()
    if len(partes) == 1:
        titulo = campo
    return titulo

def normalizar_colaboradores(campo: str) -> list:
    campo = campo.strip('"').strip()
    colaboradores = []
    partes = campo.split("-")
    if len(partes) > 1:
        colabs = partes[0].split("|")
        for colab in colabs:
            colaboradores.append(colab.strip())
    return colaboradores


def normalizar_vistas(campo: str) -> int:
    resultado = 0
    if isinstance(campo, str):
        campo = campo.strip('"').lower()
        if "millones" in campo:
            numero = campo.replace("millones", "").strip().replace(",", ".")
            resultado = int(float(numero) * 1_000_000)
        elif campo.isdigit():
            resultado = int(campo)
    return resultado

def normalizar_duracion(campo: str) -> int:
    resultado = 0
    if isinstance(campo, str) and ":" in campo:
        m, s = campo.strip('"').split(":")
        resultado = int(m) * 60 + int(s)
    return resultado


def normalizar_link(campo: str) -> str:
    resultado = ""
    if isinstance(campo, str) and ("youtube.com" in campo or "youtu.be" in campo):
        resultado = campo.strip('"')
    return resultado

def normalizar_fecha(campo: str) -> str:
    resultado = None
    if isinstance(campo, str) and len(campo.split("-")) == 3:
        y, m, d = campo.strip('"').split("-")
        resultado = f"{int(y)}/{int(m)}/{int(d)}"
    return resultado
