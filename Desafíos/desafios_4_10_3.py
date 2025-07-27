#Desafío 3: Estructuras de Datos Anidadas
"""Considera un sistema de manejo de inventario para una cadena de tiendas minoristas. 
Tienes que tratar con datos de productos, tiendas, empleados, y transacciones, 
donde cada tienda podría tener múltiples productos y empleados. 
Gestionar estas relaciones con TADs podría ser ineficiente y propenso a errores."""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto {self.nombre}, Precio {self.precio}, Cantidad {self.cantidad}"
    

"""class Empleados:
    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.edad}, Cargo {self.cargo}"""

class Catalogo:
    def __init__(self):
        self.productos = []

    def alta_producto(self, producto):
        self.productos.append(producto)
        print(f"El producto '{producto.nombre}' fue ingresado correctamente ")

    def baja_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"El producto '{producto.nombre}' fue eliminado correctamente")
                return
            else:
                print(f"El producto '{producto.nombre}' no fue encontrado")
                return

    def modificar_producto(self, nombre, new_nombre=None, new_precio=None, new_cantidad=None):
        for producto in self.productos:
            if producto.nombre == nombre:
                if new_nombre:
                    producto.nombre = new_nombre
                if new_precio is not None:
                    producto.precio = new_precio
                if new_cantidad is not None:
                    producto.cantidad = new_cantidad

                print(f"El producto {nombre} fue modificado correctamente")
                return

        print(f"El producto '{nombre}' no se encontró")
        return

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos guardados")
        else:
            print("El catalogo:")
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"Producto fue encontrado con éxito : {producto}")

    def ordenar_precio(self):
        self.productos.sort(key=lambda producto: producto.precio)
        print("Productos ordenados por precio:")

def menu_productos():
    catalogo = Catalogo()

    while True:
        print("\n1. Alta Producto")
        print("2. Baja Producto")
        print("3. Modificar Producto")
        print("4. Mostrar Productos")
        print("5. Buscar Productos")
        print("6. Ordenar Productos")
        print("7. Salir")

        print("Ingresar número del 1 al 7 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            print("Ingresar los datos del producto. Estos son Nombre, Precio y Cantidad")
            nombre = input()
            precio = float(input())
            cantidad = int(input())
            producto = Producto(nombre, precio, cantidad)
            catalogo.alta_producto(producto)

        elif nav_menu == "2":
            print("Ingresar el nombre del producto a borrar")
            nombre = input()

            catalogo.baja_producto(nombre)

        elif nav_menu == "3":
            print("Ingresar el nombre del producto que se desea modificar")
            nombre = input()
            print("Ingresar los datos que se desea modificar")
            nuevo_nombre = input()
            nuevo_precio = input()
            nueva_cantidad = input()

            nuevo_nombre = nuevo_nombre if nuevo_nombre else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            catalogo.modificar_producto( nombre, nuevo_nombre, nuevo_precio, nueva_cantidad)

        elif nav_menu == "4":
            catalogo.mostrar_productos()

        elif nav_menu == "5":
            print("Ingresar el nombre del producto")
            nombre = input()
            catalogo.buscar_producto(nombre)

        elif nav_menu == "6":
            catalogo.ordenar_precio()
            catalogo.mostrar_productos()

        elif nav_menu == "7":
            print("saliendo")
            break

        else:
            print("Ingresar número del 1 al 7")

if __name__ == "__main__":
    menu_productos()