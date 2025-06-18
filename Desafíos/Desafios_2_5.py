#Desafio1
#Escriba un programa que pida al usuario su nombre y su ciudad de origen, 
# luego imprima un saludo personalizado con esa información.

"""

#se pide el nombre
print("ingresar nombre")
nombre = input()
#se pide la ciudad de origen
print("ingresar ciudad de origen")
c_ori = input()
#se muestra el mensaje con las variables en un f-string
print(f"Buenos dias {nombre} dicen que en {c_ori} hace un lindo clima hoy.")

"""

#Desafio2
#Escriba un programa que pida al usuario que ingrese dos números y luego imprima 
# la suma, la resta, la multiplicación y la división de esos números.

"""

#decidi hacer un menu simple para que sea mas amena las pruebas del script
#en si es un script muy simple
while True:
    #las opciones del menu
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    #se pide un input para manejar el menu
    print("Ingresar número del 1 al 5 para operar el menu")
    nav_menu = input()
    
    if nav_menu == "1":
        #se piden dos números y se guardan en variables
        print("ingresar el primer número de la suma")
        num_1 = int(input())
        print("ingresar el segundo número de la suma")
        num_2 = int(input())
        #se guarda la suma en una teercera variable
        num_3 = num_1 + num_2
        #se muestra el resultado llamando a las variables
        print("la suma de", num_1, "+", num_2, "es:", num_3)
    
    elif nav_menu == "2":
        #se piden dos números y se guardan en variables
        print("ingresar el primer número de la resta")
        num_4 = int(input())
        print("ingresar el segundo número de la resta")
        num_5 = int(input())
        #se guarda el resultado de la resta en una tercer variable
        num_6 = num_4 - num_5
        #se muestra el resultado
        print("la resta de", num_4, "-", num_5, "es:", num_6)

    elif nav_menu == "3":
        print("ingresar el primer número de la multiplicación")
        num_7 = int(input())
        print("ingresar el segundo número de la multiplicación")
        num_8 = int(input())
        num_9 = num_7 * num_8
        print("la multiplicacion de", num_7, "*", num_8, "es:", num_9)

    elif nav_menu == "4":
        print("ingresar el primer número de la división")
        num_10 = int(input())
        print("ingresar el segundo número de la división")
        num_11 = int(input())
        num_12 = num_10 / num_11
        print("la division de", num_10, "/", num_11, "es:", num_12)
            
    elif nav_menu == "5":
        #para salir del menu, por defecto, una vez que se usa una opción del menu, el script sigue corriendo
        #solo se sale con un break o parando la compilación del programa
        print("saliendo")
        break
    
    else:
        print ("ingresar un número del 1 al 5")


"""        


#Desafio3
#Escriba un programa que pueda tomar los detalles de los productos (nombre, cantidad, precio) 
#y produzca una factura bien formateada.

"""

#se pide el nombre de la persona
print("Ingrese su nombre:")
nom_per = input()

#se pide la cantidad de productos
print("Ingrese la cantidad de productos a ingresar:")
num_pro = int(input())

#se crea una lista vacia para guardar los productos, decidi usar una lista para mantener el orden de los productos
productos = []
#se inicializa una variable con valor 0 para luego asignare un valor y también para calcular el iva
sub_tot = 0

#búcle para ingresar productos en la lista
#se ingresan la cantidad especificada en num_pro con el método range() de python 
#Es decir si se especifica que se quieren ingresar 5 productos, va permitir ingresar 5 productos
for i in range(num_pro):
    #se pide el primer producto
    #el +1 es para que los incluya a todos y no pare en el ultimo producto sin mostrarlo
    print(f"\nProducto {i + 1}")
    #se pipde el nombre del producto
    print("Nombre del producto:")
    nombre = input()

    #se pide la cantidad del producto, no es lo mismo con la cantidad de productos a comprar
    #son 5 productos (por ejemplo) y se quiere 2 de cada productos
    print("Cantidad a comprar:")
    cant_pro = int(input())

    #decidi poner el precio en float porque al comprar es mucho mas probable terminar con decimales
    print("Precio individual del producto:")
    prec_uni = float(input())

    #variable para calcular el precio en base a la cantidad
    #cant_pro es la cantidad de producto y prec_uni es el valor individiual del producto en cuestión
    tot_prod = cant_pro * prec_uni
    #en este caso es +=, en lugar de = solo, porque, 
    #es para acumular el precio total y no quedar solo con el ultimo valor
    sub_tot += tot_prod

    #se ingresan los productos en la lista con el .append
    productos.append({
        "nombre": nombre,
        "cantidad": cant_pro,
        "precio_individual": prec_uni,
        "precio_total": tot_prod
    })

#se calcula el iva completo
iva = sub_tot * 0.21
#se calcula el precio del producto mas el iva para ver el precio final
total = sub_tot + iva

#se muestra la factura con \n para que haga saltos de página, es decir que se muestre en renglones diferetes
print("\nFACTURA")
#nombre de la persona
print("\nCliente:", nom_per)
#búcle para mostrar los productos
#los productos se muestran en un bucle por dos motivos:
#primero, para poder mostrar la cantidad que se quiera sin necesidad de escribirlo manualmente
#segundo, porque los productos estan guardados en una lista. Para mostrar todo el contenido de una lista
#hay que recorrerla de algúna forma.
for i in productos:
    #se muestra la variable i, para que le ponga número a cada producto
    #:.2f significa que va a mostrar 2 puntos después de la coma, por ejemplo 20,24
    print(f"- {i['nombre']}: {i['cantidad']} x {i['precio_individual']} = {i['precio_total']:.2f}")

#se muestra el precio
print(f"\nSubtotal: {sub_tot:.2f}")
print(f"\nIVA: {iva:.2f}")
print(f"\nTotal: {total:.2f}")

"""