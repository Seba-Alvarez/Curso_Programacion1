#Desafío extra: 
#Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, 
# determine cuál de ellos es el mayor. Considera la posibilidad de que algunos o todos los números sean iguales. 
# El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales.
# Desafío extra

a = int(input("primer numero"))
b = int(input("segundo numero"))
c = int(input("tercer numero"))

if a == b == c:
    print("los tres numeros son iguales")
elif a == b:
    print("el primer y segundo numero son iguales")
elif b == c:
    print("el segundo y tercer numero son iguales")
elif a == c:
    print("el primer y tercer numero son iguales")
else:
    print("nignuno de los numeros son iguales")

print(f"el mayor numero es: {max(a,b,c)}" )

#Desafío 72: 
#Un sistema de inventario tiene una lista con los códigos de productos. 
# Desarrolla un programa que permita al usuario introducir un código de producto y que determine 
# si ese código está en la lista. Si el código se encuentra, el programa debe devolver 
# la posición en la que aparece; si no está, debe mostrar un mensaje 
# indicando que no se ha encontrado el código.

cod_prod = [1010,2020,3030,4040,5050,6060,7070,8080,9090, 1010]
pos = []

cod_ing = int(input("ingresar codigo de producto"))

for i in range(len(cod_prod)):
    if cod_prod[i] == cod_ing:
        pos.append(i)
if pos: print(f"codigo {cod_ing} encontrado en las posiciones {pos}")
else: print("codigo no encontrado")


#Desafío 73: 
#Tienes una lista de números en la que algunos elementos están repetidos. 
# Desarrolla un programa que elimine todos los elementos duplicados y deje 
# únicamente una aparición de cada uno. La salida debe mostrar la 
# lista original y la lista sin duplicados.

lis_ori = [4,2,5,3,4,5,5,4,2,3]
lis_fil = []

for i in lis_ori:
    if i not in lis_fil:
        lis_fil += [i]

print (f"lista original: {lis_ori} \n lista sin duplicados {lis_fil}")

#Desafío 74: 
#Tienes dos listas de números enteros de diferentes longitudes. 
# Desarrolla un programa que sume los elementos de las listas en las posiciones correspondientes. 
# Si una lista es más corta que la otra, los elementos que falten deben considerarse como 0 en la suma.

lis_1 = [1,2,3]
lis_2 = [4,5]
res = []

max_len = max(len(lis_1), len(lis_2))

re_1 = lis_1 + [0] * (max_len - len(lis_1))
re_2 = lis_2 + [0] * (max_len - len(lis_2))

for i in range(max_len):
    res.append(re_1[i] + re_2[i])

print(f"resultao de las operaciones es: {res}")

#Desafío 75: 
#Usa una "list comprehension" para crear una lista llamada potencias que contenga 
# las potencias de 2 de los números del 0 al 9 (es decir, 2 elevado a la potencia de cada número). 
# Imprime la lista resultante.

pot = [2**i for i in range(10)]
print(f"portencias desde el hasta el 10: {pot}")