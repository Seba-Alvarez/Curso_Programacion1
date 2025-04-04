"""Desafío 1: Suma de Dos Números (tema1-1des1)
Objetivo: Crear un programa que sume dos números predefinidos y muestre el resultado."""

#Se declara la primera variable y se pide el primer número
print("Entre el primer numero ")
var1 = int(input())
#Se declara la segunda variable y se pide el segundo número
print("Entre el segundo numero ")
var2 = int(input())
#Se suman las dos variables
var3 = var1 + var2
#Se imprime por consola el resultado
print("La suma de", var1, "y", var2, "es", var3)

"""Desafío 2: Calcular el Área de un Rectángulo con Presentación (tema1-1des2)
Objetivo: Escribir un programa que, utilizando valores predefinidos, calcule el área de un rectángulo y
presente los resultados de manera amigable utilizando texto."""

#Print vacío para generar espacios cuando se muestra por consola
print("")
print("")

#Eleji mostrar el mensaje por variable, para poder pegarlo completo
print(var1)

#Print para generar espacio
print("")

# Se pide el largo
print("Entre el largo del cuadrado ")
var2 = int(input())
# Se pide el ancho
print("Entre el ancho del cuadrado ")
var3 = int(input())
# Se hace la cuenta
var4 = var2 * var3

print("El area de su rectángulo es", var4)