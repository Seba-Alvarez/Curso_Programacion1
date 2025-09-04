#Desafío extra: 
#Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, 
# determine cuál de ellos es el mayor. Considera la posibilidad de que algunos o todos los números sean iguales. 
# El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales.
# Desafío extra

#se piden los inputs para los numeros
a = int(input("primer numero"))
b = int(input("segundo numero"))
c = int(input("tercer numero"))

#se verifica si los tres numeros son iguales con ==
if a == b == c:
    print("los tres numeros son iguales")
#se verifica si a y b son iguales pero sin c ser igual
elif a == b:
    print("el primer y segundo numero son iguales")
#se verifica si a y b son iguales pero si a ser igual
elif b == c:
    print("el segundo y tercer numero son iguales")
#se verifica si a y c son iguales pero si b ser igual
elif a == c:
    print("el primer y tercer numero son iguales")
#para cuando ninguno de los numeros son iguales
else:
    print("nignuno de los numeros son iguales")
#se le pasa al metodo max las tres variables con los numeros
#max siempre va a devolveer el mayor numero de los que se le pasen como argumento
print(f"el mayor numero es: {max(a,b,c)}" )

#Desafío 72: 
#Un sistema de inventario tiene una lista con los códigos de productos. 
# Desarrolla un programa que permita al usuario introducir un código de producto y que determine 
# si ese código está en la lista. Si el código se encuentra, el programa debe devolver 
# la posición en la que aparece; si no está, debe mostrar un mensaje 
# indicando que no se ha encontrado el código.

#se define una lista con los codigos de productos
cod_prod = [1010,2020,3030,4040,5050,6060,7070,8080,9090, 1010]
#una lista vacia para guardar los indices de las posiciones
#eso es para cuando se da mas de una posición y que no muestre solo la primera ocurrencia
pos = []

#se pide el codigo por input, en este caso se pide un integer
#porque los elementos de la lista tambien fueron definidos como int
cod_ing = int(input("ingresar codigo de producto"))

#se recorre el rango de la lista que contiene los codigos de los productos
#no se modifica la lista original
for i in range(len(cod_prod)):
    #aca se verifica en cada iteracion del bucle si el codigo de la lista es el mismo que
    #el ingresado por consola, si coincide se guarda el item actvual en la lista vacia
    #para mostrar luego todas las posiciones
    if cod_prod[i] == cod_ing:
        #aca se agrega a la lista usando el metodo append
        pos.append(i)

#se pone el mostrar afuera del bucle para que lo muestre una sola vez
#el f-string, en este caso,  es para concatenar de forma que sea mas legible
if pos: print(f"codigo {cod_ing} encontrado en las posiciones {pos}")
#este caso es por si no se encuentra, por lo mismo se pone afuera del for para que
#no lo repita en cada iteracion del bucle
else: print("codigo no encontrado")


#Desafío 73: 
#Tienes una lista de números en la que algunos elementos están repetidos. 
# Desarrolla un programa que elimine todos los elementos duplicados y deje 
# únicamente una aparición de cada uno. La salida debe mostrar la 
# lista original y la lista sin duplicados.

#lista original
lis_ori = [4,2,5,3,4,5,5,4,2,3]
#lista vacia para guardar los duplicados
lis_fil = []

#se recorre cada item de la lista original
for i in lis_ori:
    #se verifica si no estan en la lista vacia
    #esto es para poner solo la primera iteracion de cada elemento
    #es decir, eliminar los duplicados
    if i not in lis_fil:
        # Se agrega el elemento al final de la nueva lista si no se agrego antes
        lis_fil.append(i)

#se muestra la lista oroiginal y la que no tiene duplicados
print (f"lista original: {lis_ori} \n lista sin duplicados {lis_fil}")

#Desafío 74: 
#Tienes dos listas de números enteros de diferentes longitudes. 
# Desarrolla un programa que sume los elementos de las listas en las posiciones correspondientes. 
# Si una lista es más corta que la otra, los elementos que falten deben considerarse como 0 en la suma.

#primera lista
lis_1 = [1,2,3]
#segunda lista de menor tamño que la primera
lis_2 = [4,5]
#lista vacia para guardar los resultados
res = []

#se guarda el largo de cada lista en una variable usando len
max_len = max(len(lis_1), len(lis_2))

#se "rellena" con 0 para que las listas sean del mismo tamaño
#len(lis_n), saca la longitud actual de la lista 
#max_len - len(lis_,), resta la longitud de la lista con mas elementos y se la resta a la lista
#entonces se sabe cuantos 0 se necesita poner a la lista
#[0] * (), genera una lista de 0s, con la cantidad calculada
#lis_1 + [0] * (), concatena la lista original con los 0s generados
#asi se forma una lista de longitud igual a max_len
#esto se repite con ambas listas
re_1 = lis_1 + [0] * (max_len - len(lis_1))
re_2 = lis_2 + [0] * (max_len - len(lis_2))

#aca es donde se hace la suma de cada elemento
#cada iteración del bucle suma los elementos de la misma posicion por indice
#y los agrega a la lista vacia para mostrar los resultados
for i in range(max_len):
    res.append(re_1[i] + re_2[i])

#se muestran la lista que contiene los resultados
print(f"resultado de las operaciones es: {res}")

#Desafío 75: 
#Usa una "list comprehension" para crear una lista llamada potencias que contenga 
# las potencias de 2 de los números del 0 al 9 (es decir, 2 elevado a la potencia de cada número). 
# Imprime la lista resultante.

#las list comprehension o comprension de listas ofrecen una sintaxis mas corta cuando se quiere generar una nueva
#lista basada en los valores de una lista existente.
#https://www.w3schools.com/python/python_lists_comprehension.asp
#esto se hace en tres partes, el input, la coleccion y la condicion
#es decir, lo que se hace, para quien y en que condicion
#para este ejemplo, para los factoriales de los numeros pares, para los numeros del 2 al 10,
#aca no se esta especificando una condicion porque el desafio no lo pide
pot = [2**i for i in range(10)]
#aca se muestra el resultado de la lista
print(f"portencias desde el hasta el 10: {pot}")