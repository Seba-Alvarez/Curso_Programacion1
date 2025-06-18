# procesador_texto.py

def contar_palabras(texto):
    return len(texto.split())

def verificar_ortografia(texto):
    # Simulamos una función que verifica la ortografía.
    # En una aplicación real, esto podría ser más complejo.
    return "Ortografía verificada."

def ajustar_margenes(texto, margen_izquierdo=10, margen_derecho=10):
    return ' ' * margen_izquierdo + texto + ' ' * margen_derecho