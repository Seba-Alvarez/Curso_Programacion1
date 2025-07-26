#Desafío 1: Sistemas con Múltiples Entidades Interconectadas
"""Imagina un sistema de gestión de biblioteca que maneja libros, usuarios, préstamos y multas. 
Usar TADs separados para cada uno de estos elementos podría complicar 
la interacción y gestión de relaciones entre ellos."""

libros = ["libro1","libro2","libro3","libro4","libro5"]
libros_backup = list(libros)

usuarios = ["user1","user2","user3","user4","user5"]
usuarios_backup = list(usuarios)

prestamos = {}
contador_prestamos=1
multas = {}
contador_multas=1

#region libros
def agregar_libros(libro):
    libros.append(libro)
    libros_backup.append(libro)

def borrar_libros(libro):
    if libro in libros_backup:
        libros_backup.remove(libro)

def modificar_libros(libro_act, libro_new):
    if libro_act in libros_backup:
        index = libros_backup.index(libro_act)
        libros_backup[index] = libro_new
        print(f"Libro {libro_act} modificado por {libro_new}.")
    else:
        print(f"Libro {libro_act} no encontrado.")

def listar_libros():
    return libros_backup

#endregion

#region user
def agregar_user(user):
    usuarios.append(user)
    usuarios_backup.append(user)

def borrar_user(user):
    if user in usuarios_backup:
        usuarios_backup.remove(user)

def modificar_user(user_act, user_new):
    if user_act in usuarios_backup:
        index = usuarios_backup.index(user_act)
        usuarios_backup[index] = user_new
        print(f"Libro {user_act} modificado por {user_new}.")
    else:
        print(f"Libro {user_act} no encontrado.")

def listar_user():
    return usuarios_backup

#endregion

#region prestamo
def agregar_prestamo(user, libro):
    global contador_prestamos
    if user in usuarios_backup and libro in libros_backup:
        prestamos[contador_prestamos] = (user, libro)
        contador_prestamos += 1
    else:
        print("Error")

def borrar_prestamo(id_prestamo):
    if id_prestamo in prestamos:
        del prestamos[id_prestamo]
        print(f"Prestamo con ID {id_prestamo} eliminado.")
    else:
        print("ID de préstamo no encontrado.")

def modificar_prestamo(id_prestamo, nuevo_usuario, nuevo_libro):
    if id_prestamo in prestamos:
        if nuevo_usuario in usuarios_backup and nuevo_libro in libros_backup:
            prestamos[id_prestamo] = (nuevo_usuario, nuevo_libro)
        else:
            print("Error")
    else:
        print("Prestamo no encontrado.")

def listar_prestamos():
    if not prestamos:
        print("No hay prestamos")
    else:
        return prestamos

#endregion

#region multas
def agregar_multa(user, libro):
    global contador_multas
    if user in usuarios_backup and libro in libros_backup:
        multas[contador_multas] = (user, libro)
        contador_multas += 1
    else:
        print("Error")

def borrar_prestamo(id_multa):
    if id_multa in multas:
        del multas[id_multa]
        print(f"Multa con ID {id_multa} eliminado.")
    else:
        print("ID de multa no encontrado.")

def modificar_prestamo(id_multa, nuevo_usuario, nuevo_libro):
    if id_multa in multas:
        if nuevo_usuario in usuarios_backup and nuevo_libro in libros_backup:
            multas[id_multa] = (nuevo_usuario, nuevo_libro)
        else:
            print("Error")
    else:
        print("Prestamo no encontrado.")

def listar_prestamos():
    if not multas:
        print("No hay multas")
    else:
        return multas

#endregion
