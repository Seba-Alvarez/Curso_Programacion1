#region DISCLAIMER

#Cabe aclarar que esta "calculadora" está hecha para convertir proposiciones informales
# como esta -p o no q y si r entonces p. Si se usara el equivalente en formal 
# -(p∨¬q)∧(r→p) el programa no va a funcionar porque no tiene soporte, no va a convertir
#  ¬q a not q, le va a mandar ¬q a python y python no va a ender nada.


#re es para evitar usar replace() y que remplace cosas que
#no se quieren remplazar, como por ejemplo en la
#proposición si la noche noche es negra, entonces está oscuro
#no camie el 'no' en noche por el 'no' de not
import re

#endregion

#region Valor de verdad
#se define la función y que se le va a pasar un argumento por parámetro
def val_ver(nom):
    #while para poder aplicarlo a todos los casos
    while True:
        #res es para controlar que se ponga algunas de estas opciones
        #el punto lower es para que siempre lo ponga en minuscula
        res = input().strip().lower()
        #verificación que se ingrese true
        if res == "v" or res == "t" or res =="1":
            return True
        #verificación para que se ingrese false
        elif res == "f" or res == "0":
            return False
        #si se ingresa "mayonesa" o algo en ese estilo, va a este else
        else:
            print("ingresar verdadero o falso")
#endregion

#region Verificar parentesis
#se define la función donde se le pasa una expresión como argumento
#esta función es para poder poner paréntesis
def par_bien_p(expr):
    #variable vacía para contar
    c = 0
    #aca se recorre a la frase para chequear los paréntesis
    for i in expr:
        #el +=1 y -=1 es para modificar el número final del contador
        # 0 += 1 termina siendo 1, a menos que se cambie en con la condición del for 
        #si encuentra este paréntesis ( suma 1 al contador
        if i == "(": 
            c += 1
        #si encuentra este paréntesis ) resta 1 al contador
        elif i ==")": 
            c -=1
        #verifica si el contador es mayor a 0 y retorna falso, para avisar que no esta balanceado
        if c < 0:
            return False
    #para que salga del for y se pueda volve a usar en otro lado
    return c == 0
#endregion

#region Ordenar tupla
#esto es para ordenar el diccionario de forma descendente
#para poder evitar, por ejemplo, que en "si y solo si" remplace solo el primer separado en lugar de toda la expresión
#use una tupla para que este siempre ordenada y no se pueda cambiar, dejando los remplazos fijos
#esto le quita mantenibilidad al código, pero es un proyecto personal educativo, no para una empresa
def ordenar(tupla):
    #ordena la tupla de mayor a menor
    #-len es para que vaya todo el largo de la tupla
    #tupla[0] es para que empiece en la primera posición de la tupla
    return -len(tupla[0])
#endregion

#region Diccionario con remplazos
#diccionario con todos los remplazos para que python interprete "no" o "¬" como not
remp = {
    "no": "not", "negacion": "not",
    "y": "and", "disyuncion": "and",
    "o": "or", "disyunción": "or",
    #no puse entonces por la forma en la que python lo escribe not p or q
    #siendo que ya hay not y or, las implicaciones las manejo mas abajo
    "si y solo si": "==", "bicondicional": "==", "doble implicación": "==",
    #si bien xor no se representa asi como tal, para no tener que usar toda la formula y complicarla a mas
    #le pedi a chatgpt que me diera una alternativa
    # me dijo que usara esto != que significa distintos, siendo que la disyunción exclusiva significa que uno es v y el otro es f
    # asi se verifica si son distintos, lo cual con datos booleanos, es lo mismo que chequear si son v o f
    # al chequear si p es distinto de q, se sabe si es v o f en función de la diferencia con p 
    "xor":"!=", "disyunción exlcusiva": "!=",
    #True y False tienen que ir en mayusculas para que cuando se pase a código python entienda que es bool return True, en lugar de var true
    "verdadero":"True" , "tautologia":"True",  
    "falso":"False" ,"contradiccion":"False",
}
#endregion

#region Armar la proposicion

#proposiciones simples o atómicas son p, q, r, s, etc
print("definir cantidad de proposiciones atÓmicas")
#aca se pide un input numérico que van a ser la cantidad de proposiciones atómicas
#en esto pienso cada vez que alguien dice proposición atómica https://www.youtube.com/watch?v=sDfPGknbPgs
pq = int(input())
#se crea un diccionario vacío
hom = {}
#se usa el for para llenar la tupla
#se recorre la cantidad de veces que se ingresa en pq
for i in range(pq):

    print("ingresar proposición:")
    #este nom es para usar la función def_val
    #el strip es para que quede en minuscula
    nom = input().strip()
    print(f"valor de {nom}:")
    #se agrega la v.a al diccionario usando la función para verificar que sea adecuada
    hom[nom] = val_ver(nom)

#se pide la proposición lógica como (p y q) entonces p
print("ingresar la proposición lógica")
#el .lower es para pasar lo que se escriba a minúscula
exp = input().lower()


#remplazo de conectores lógicos con un for
#el for tiene dos valores porque los diccionarios tienen pares clave-valor
#i representa la clave y j repsenta el valor.
#sorted es un método de python para ordenar, se le pasan
# un objeto iterable(para ordenar), una key (una función) y el reverse es para el orden
#por defecto el reverse es false, por lo cual se puede evitar si se desea ese orden 
#False es ascendente y True es para descendente
#remp.items son los items del diccionario remp
for i, j in sorted(remp.items(), key=ordenar):
    #exp es la expresión ingresada
    #re.sub es para usar la librería importada que reemplaza los símbolos
    #la sintáxis es re.sub(patrón, remplazo, string)
    #patrón es la expresión que se busca substituir
    #remplazo es lo que va a substituir la expresión deseada
    #string es donde busca y hace el remplazo
    #r es para un raw string y f es para un f-string, \b busca el final o comienzo una palabra
    #escape convierte caracteres en texto normal, esto es por si se usan los carácteres en lugar de palabras
    exp = re.sub(rf'\b{re.escape(i)}\b', j, exp)

#esto maneja las implicaciones, la verdad se lo pedí a chatGPT porque la línea de arriba me complicó muchisimo
# (.+?) es un grupo de captura que captura cualquier cadena de texto que esté antes del conector lógico
#también significa uno o más caracteres
#\*s captura cualquier cantidad de espacios en blanco en caso de existir
#Esto (.+) es otro grupo de captura que captura la parte de la proposición después del conector lógico
#estas dos lineas me dieron muchisimos problemas, demasiados
#estas tres líneas me dieron unos problemas horribles.
#esto maneja los paréntesis
exp = re.sub(r'\bsi\s+(.+?)\s+entonces\s+(.+)', r'not (\1) or (\2)', exp)
#esto es para manejar si se escribe solo entonces
exp = re.sub(r'(.+?)\s+entonces\s+(.+)', r'not (\1) or (\2)', exp)
#esto es para las bicondicionales
#esto ve que los paréntesis en las bicondicionales e implicaciones estén bien colocaodos
#esta línea casi me saca canas verdes, creo que perdi un par de años de vida con esto
#ni con la ayuda de gpt se hizo facil, originalmente las implicaciones se manejaban en la línea de arriba
#pero viendo que tuve muchisimos problemas para que convirtiera p o no q y si r entonces p
#hubo muchos fallos, desde poner todo en parentesis al pasarlo a python
#despues que tuve bien los parentesis no me pasaba bien el "entonces", en lugar de pasarlo a python le pasaba entonces
#al final dividi en dos los re.sub y lo logré poner bien
exp = re.sub(r'(.+?)\s*(implicacion)\s*(.+)', r'not (\1) or (\3)', exp)
exp = re.sub(r'(.+?)\s*(si y solo si|bicondicional|doble implicación)\s*(.+)', r'(\1) == (\3)', exp)

#endregion

#region Verificar proposicion

#verificar si tiene bien puestos los paréntesis y si es verdadero o falso

#Imprimir la proposición para ver porque no anda esta cafetera(depurar o debuggear o debugging)
#ESTA LÍNEA FUE UNA DE LAS DOS LÍNEAS MAS UTILES DE EL PROGRAMA
print(f"Proposición procesada: {exp}") 

#si no está bien balnceado, esto se verifica en la función
if not par_bien_p(exp):
    print("paréntesis mal puestos")
else:
    #try, except es para manejo de excepciones
    #se corre lo que hay en el try, si no ocurren errores se continua con el programa
    #si hay errores pasa al catch y no permite que el programa continue, en este caso es el final
    # y solo muestra un print, pero en programas grandes se nota mas lo útil que es
    try:
        #eval retorna el resultado de la proposición
        #la sintaxis es eval(expresión, global, local)
        #expresión es el string a evaluar
        #global son variables o funciones de scope global, en este caso va a devolver True o False
        #local son variables o funciones de scope local, en este caso contiene los valores de verdad
        prop_val = eval(exp, {}, hom)
        #se muestra si la proposición es verdadera o falsa
        #prop_val es el resultado de la proposición
        #Es True o False, entences, por defecto se muestra verdadera, si no lo fuera va al if y muestra lo opuesto
        print("La proposición es verdadera"
              if prop_val else 
                "La proposición es falsa")
    #este error es mas que nada un chiste, pero try except es super util a la larga
    #quizá se me escapó decir try catch en vez de try except en algún lado, si pasó, pido disculpas
    #asi como pido disculpas por las faltas de ortografía, es tarde y tengo mucho sueño
    #esta e es para ver lo que está transformando, me sirvió mucho para debuggear
    #ESTA ES LA OTRA LÍNEA, ESTA FUE INDISPENSABLE TAMBIÉN
    except Exception as e:
        print("error 404, no hay conexión a internet", e)

#endregion

#region Proposiciones intentadas

#p o no q y si r entonces p

#p xor q

#p entonces q

#p y q

#p o q

#p si y solo si q
 
#p no q, que sería p¬q no existe como tal en python, hay que escribirla asi p y no q

#no estoy seguro si esto está bien formulado "funciona", pero no se si se usan tautologías y contradicciones en la proposición misma
#p verdadero q, que sería p⊤q no existe como tal en python, hay que escribirla asi p y verdadero y q
#p falso q, que sería p⊥q no existe como tal en python, hay que escribirla asi p y falso y q

#endregion
