#Desafío extra: 
#Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, 
# determine cuál de ellos es el mayor. Considera la posibilidad de que algunos o todos los números sean iguales. 
# El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales.
# Desafío extra

#se piden los números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

#si son los 3 iguales
if a == b == c:
    print("Todos los números son iguales.")
#si dos de ellos son iguales
elif a==b or a==c or b==c:
    print("dos de los números ingresados son iguales")
else:
    #se busca el mayor con max
    mayor = max(a, b, c)
    #se imprime el mayor por pantalla
    print(f"El número mayor es: {mayor}")

#Desafío 72: 
#Un sistema de inventario tiene una lista con los códigos de productos. 
# Desarrolla un programa que permita al usuario introducir un código de producto y que determine 
# si ese código está en la lista. Si el código se encuentra, el programa debe devolver 
# la posición en la que aparece; si no está, debe mostrar un mensaje 
# indicando que no se ha encontrado el código.

#Desafío 73: 
#Tienes una lista de números en la que algunos elementos están repetidos. 
# Desarrolla un programa que elimine todos los elementos duplicados y deje 
# únicamente una aparición de cada uno. La salida debe mostrar la 
# lista original y la lista sin duplicados.

#Desafío 74: 
#Tienes dos listas de números enteros de diferentes longitudes. 
# Desarrolla un programa que sume los elementos de las listas en las posiciones correspondientes. 
# Si una lista es más corta que la otra, los elementos que falten deben considerarse como 0 en la suma.
# Desafío 74

#Desafío 75: 
#Usa una "list comprehension" para crear una lista llamada potencias que contenga 
# las potencias de 2 de los números del 0 al 9 (es decir, 2 elevado a la potencia de cada número). 
# Imprime la lista resultante.