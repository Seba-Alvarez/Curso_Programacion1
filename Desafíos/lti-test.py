#se define una variable con mi nombre, como se pide la letra
#si se quisiera hacer dinámico se usaría un input, algo asi:
#nom = input("ingresar nombre")
nom = "Sebastián"
#decidí usar un f-string para poder incluir directamente el nombre de la variable sin concatenar con comas
#esto por si se quisiera hacer dinámico (con el input) 
#o si se quisiese cambiar el nombre guardado en la variable
#Al mostrar texto (un string en este caso) existe lo que se llaman caracteres de escape 
#(https://www.w3schools.com/python/gloss_python_escape_characters.asp)
#esto caracteres tienen diferentes funciones, en este caso se usaron dos:
#El primer caracter es \t que hace un tab o tabulador para indentar.
#El segundo, \n que hace un salto de línea.
#No quise usar un salto de al principio (Antes del bienvenido) porque técnicamente
#serían 3 lineas, en lugar de las dos que se piden en la consigna.
#los "espacios vacios" son caracteres y al poner un salto de linea (como en el código original)
#se muestra la frase en 3 líneas en lugar de 2.
print(f"\nBienvenido \t{nom} \nal Curso de Programación")