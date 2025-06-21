# formato_texto.py

#usando codigos de escape ansii permiten cambiar el formato de los textos
#muchos cmd los "entienden"
#las secuencias siempre empiezan por \033[ , luego algun código que diga el estilo y terminan con alguna letra

#link a una lista de código ansii:
    #https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences?utm

def negrita(texto):
    #por ejemplo aca, se esta usando un f string para formatear todo el texto
    #\033[1m significa que el texto empiece en nagrita
    #{texto} es el parámetro que se le pasa a la función
    #\033[0m aca termina
    return f"\033[1m{texto}\033[0m"

#es el [xm donde x es el identificador ansii
def italica(texto):
    return f"\033[3m{texto}\033[0m"

def subrayado(texto):
    return f"\033[4m{texto}\033[0m"

def tachado(texto):
    return f"\033[9m{texto}\033[0m"
