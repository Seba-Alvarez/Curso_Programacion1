#region librerias

#aca se importan las librerías para poder usar las funcionalidadaes que no vienen nativas con python
#ademas se agregan los as name para no tener que poner el nombre completo de la libreria cada vez que se usa.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#endregion

#region creación del tablero
#se le pasan las filas, columnas y la probabilidad de vida
#los valores son 0 o 1, donde 0 significa que las células estan muertas
#1 significa que estan vivas
#la probabilidad de vida es la probabilidad de que las células esten vivas, en este caso un 20%
#este quiere decir que, en este caso, el 20%(0.2) de las células van a empezar vivas, si se cambia este número cambia el tablero
#mientras que prob vida es la probabilidad de que las células esten vivas
def crear_tablero(filas, columnas, prob_vida=0.2):
    #el tablero se hace de forma random con random.choice que retorna elementos random, en este caso, 0 o 1.
    #el tamaño del array se define por el size, es decir los valores de las filas y las columnas
    #si por ejemplo, ambos valores son 10, va a ser un array de 10x10 (con valores entre 0 y 1)
    #1-prob vida significa la probabilidad de que las células esten muertas (las probabilidades tienen que sumar 1, que significa el 100%)
    #por ejemplo, si se tira una moneda la probabilidad de que salga cara es de 50%, esto es 1(la posibilidad)-0.5(la chance de que salga cara) = 0.5(la posibilidad que salga cruz)
    return np.random.choice([0, 1], size=(filas, columnas), p=[1 - prob_vida, prob_vida])
#endregion

#region actualizar el tablero (reglas)

#se define la función, que se le va a pasar un tablero (un array con 0's y 1's) por parámetro
#esta función calcula los tableros, se podría decir que aplica las reglas del juego
def actualizar_tablero(tablero):
    #aca se forma el array
    #se piden los valores de las filas y las columnas con .shape
    #.shape es un método usado para obtener las dimensiones de un array
    filas, columnas = tablero.shape
    #aca se crea el nuevo tablero vacio con zeros, con el tamaño especifico del array (sus filas y columnas)
    #dtype le está diciendo a python que trate los datos del array como objetos de tipo integers(https://numpy.org/doc/2.2/reference/arrays.dtypes.html)
    nuevo_tablero = np.zeros((filas, columnas), dtype=int)

    #búcles for anidados para recorrer el tablero porque es un array multidimesional
    #el primer for es para recorrer las filas, mientras que el segundo recorre las columnas
    #al estar usando numpy, python acepta directamente tuplas para las posiciones
    #numpy interpreta los valores de la tupla como indices para las dimensiones del array
    #por cada elemento del array en el rango (la cantidad de elementos de) la fila
    for i in range(filas):
        #a su vez, conformando la tupla y dando la posición de la segunda dimensión del array
        #por cada elemento del array en el rango (la cantidad de elementos de) la columna
        for j in range(columnas):
            #aca se cuentan los vecinos vivos
            #np.sum cuenta la suma de todos los valores seleccionados
            #se selecciona un subarray de 3x3 para calcular los vecinos vivos de la posción central del array, 
            # es decir, [1,1] y sus 8 vecinos
            #max (i-1,0) se asegura que no pueda ir por debajo de la fila o la columna 0
            #i es el argumento que se le pasa a max, es decir, el indice de la fila que se está iterando
            #se sabe que es la fila, porque se define en el primer for
            #i tiene el valor de la fila actual, i-1 es la que está "arriba", mientra que i+1 es la que está abajo
            #el max se usa para evitar que se salga de rango, para asegurar que el índice no sea menor que 0 (la fila mínima válida, porque no puede tener valores negativos)
            #mientras que el min, se asegura que no se pase de la ultima fila
            #filas es el número total de filas del array
            #al usar slicing, la última posición no es exclusiva
            #entonces, si se usara i+1 no tomaria el vecino de abajo, si se usa i+2 toma el vecino de abajo y termina ahi
            #el mismo proceso ocurre con las columnas, j en este caso
            #la resta final es para no tener en cuenta el valor de la posición
            #es decir, no se cuenta la célula actual, porque esto es para saber si los vecinos estan vivos, si no se resta el calculo de los vecinos quedaría mal
            #esto está definido por las reglas del juego
            vecinos = np.sum(tablero[max(i-1, 0):min(i+2, filas),
                                     max(j-1, 0):min(j+2, columnas)]) - tablero[i, j]
            #aca se aplican las reglas del "juego"
            #si la célula, de una determinada posición, está viva (es decir, su valor es 1)
            if tablero[i, j] == 1:
                #las celulas solo sobreviven si tienen vecinos vivos
                #es decir, la suma total de los otras 8 celdas que la rodean
                #pero, si tiene muchas células vecinas (mas de 3), muere por sobrepoblación (vecinos == 3)
                #asi mismo, si no tiene suficientes células vecinas, también muere, por soledad (vecinos == 2)
                if vecinos == 2 or vecinos == 3:
                    #si se cumplen las condiciones, es decir, no tener menos de 2 vecinos o mas de 3, la célula sobrevive
                    #entonces se le dan valores al nuevo tablero que se definió arriba (que antes de iniciar el "juego" está vacío)
                    nuevo_tablero[i, j] = 1
            #si la célula está muerta, es decir, su valor no es un (entonces es 0)
            else:
                #pero la célula muerta tiene exactamente 3 vecinos
                if vecinos == 3:
                    #la misma revive, entonces se crea el nuevo tablero
                    nuevo_tablero[i, j] = 1

    #retorna el tablero, mostrandolo
    return nuevo_tablero

#endregion

#region mostrar el juego

#se define una función que va a recibir 3 parámetros
#el tablero incial, es decir el array con 0's(células muertas) y 1's (células vivas)
#las generaciones, es decir, la cantidad de iteraciones que van a suceder
#los intervalos, es decir, el tiempo (en milisegundos) que va a ocurrir entre cada generación
def simular_juego(tablero_inicial, generaciones_max=200, intervalo=200):
    #crea una figura(fig) y un eje(axis) usando la libreria, esto dibuja un "gráfico" para mostrar la animación del "juego"
    #https://www.w3schools.com/python/matplotlib_subplot.asp
    fig, ax = plt.subplots()
    #se guarda una copia del tablero inicial, para no modificar el inicial, por si es necesario hacer calculos o comparaciones con el mismo
    tablero = tablero_inicial.copy()
    #aca se renderiza visualmente el array o tablero para "jugar" (lo cual se inicializa con una variable)
    #se usa ax.imshow de matlob https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html
    #cada valor del tablero (0 o 1), que esta guardado en la variable tablero, se traduce a colores con cmap
    #cmap='binary' le está diciendo a imshow que 0 es color blanco y 1 es color negro.
    #esto biene predefinido por la libreria, estos colores se pueden cambiar
    img = ax.imshow(tablero, cmap='binary')

    #se crea una lista vacia para guardar los tableros para mas adelante
    estados_previos = []
    #aca se cuentan las generaciones, es decir, cada iteración del "ciclo de vida" del "juego", además sirve para que animar pueda llevar el conteo de las generaciones
    #se guarda una lista con un solo elemento, un entero con valor 0
    #los enteros en python no son mutables, pero las listas si
    #es decir, los objetos de la clase int una vez creados tienen su espacio propio en la memoria, que no se cambia a menos que se vuelva a generar (o este repetido arriba)
    #sin embargo, las listas si se pueden cambiar, aunque también tienen un espacio de memoria definido, son un conjunto de objetos referenciados en otros lados
    #al modificar un elemento de la lista, el objeto en la memoria sigue siendo igual aunque haya cambiado el contenido
    generaciones = [0]

    #region animación

    #esta función se llama en cada frame para mostrar el contenido
    #aunque tiene un parámetro, esto indica el índice de los frames
    #en este caso no lo estoy usando explicitamente en esta función, pero la función FuncAnimation lo espera como parámetro por default
    #se podría especificar uno "vacio", pasandole un "_" pero como no lo uso es lo mismo en este contexto simple
    def animar(frame):

        #el scope o alcance, es la "zona" del programa donde una función u objeto  es visible, accesible y, a veces, modificable
        #esta variable no es local de esta función anidad, sino de la función externa simular_juego
        #esto es para que modifique la variable fuera de esta función, además, tablero está definida en la función superior (la de arriba)
        #aca se especifica que se está usando la variable que no es local de esta función, sino que es la que está afuera
        #si no se especifica, crearía una nueva variable que si fuera local a esta función y no modificaria los tableros
        nonlocal tablero
        #cada frame o iteración se le suma una generación, entonces la lista pasa a tener el valor de la generación actual
        generaciones[0] += 1
        #llama a la función que aplica las reglas y le pasa el tablero actual para "jugar"
        nuevo_tablero = actualizar_tablero(tablero)

        # Condiciones para determinar cuando el juego termina
        #usando array_equal de numpy https://numpy.org/doc/2.1/reference/generated/numpy.array_equal.html
        # se verifica si el nuevo tablero es igual al tablero anterior
        #si el tablero no cambió de generación a generación, se considera estable y termina el "juego"
        if np.array_equal(nuevo_tablero, tablero):
            #se muestra un mensaje
            print("Tablero estable. Deteniendo la simulación.")
            #termina el "juego"
            #ani es la variable que contiene la animación creada (está mas abajo)
            #event_source es el temporizador interno
            #stop() es la función de matlob para hacer que pare
            ani.event_source.stop()
        #si el tablero coincide con alguno de los ulitmos 10, se considera un búcle y para para que no corra de forma indefinida
        #np.array_equal compara si los arrays son iguales
        #es decir, si cualquiera de los ultimos 10 tableros son iguales al actual el juego para
        #estado es la variable que se está recorriendo, puede ser cualquier nombre
        #estados previos es la lista con los tableros, se piden los ultimos 10 con slicing
        elif any(np.array_equal(nuevo_tablero, estado) for estado in estados_previos[-10:]):
            #se muestra el mensaje
            print("Ciclo detectado. Deteniendo la simulación.")
            #se sale del "juego"
            ani.event_source.stop()
        #si el valor del tablero es 0, es decir que todas las células murieron, el "juego" termina
        #count_nonzero cuenta la cantidad de valores que no son 0 en el array
        #entonces, si devuelve 0, es que todas la células murieron y el "juego" terminó
        elif np.count_nonzero(nuevo_tablero) == 0:
            #se muestra el mensaje
            print("Extinción. Todas las células murieron.")
            #se sale del "juego"
            ani.event_source.stop()

        #se guarda una copia del nuevo tablero en la lista de estados previos
        #es un "agregar al historial", para que el nuevo tablero quede guardado y poder compararlo
        estados_previos.append(nuevo_tablero.copy())
        #se actualiza la variable tablero, que ahora si está en el scope de la función, para que sea el nuevo tablero
        tablero = nuevo_tablero
        #actualiza la animación con las nuevas imágenes
        #https://matplotlib.org/stable/api/image_api.html
        img.set_data(tablero)
        #devuelve la imágen, que es un requisito de FuncAnimation para actualizar solo los elementos modificados
        return [img]
    #endregion

    #aca es donde se crea la animación
    #con animation.FuncAnimation de matplotlib
    #a esta función se le tiene que pasar los siguientes parámetros
    #fig, la imágen donde se va a mostrar la animación
    #animar, que es la función anidada dentro de esta que actualiza el tablero
    #frames, es decir (en este caso, por la variable definida arriba) cuantas generaciones va a mostrar como maximo, en este caso son 200
    #intervalos, es decir el tiempo entre generación y generación
    #blit, que es para actualizar solo los elementos que cambiaron
    ani = animation.FuncAnimation(fig, animar, frames=generaciones_max, interval=intervalo, blit=True)
    #muestra el titulo con la función title de matplotlib
    plt.title("Juego de la Vida de Conway")
    #esta línea es la que muestra la ventana donde se muestra todo
    plt.show()

#endregion

#region "ejecutable"

# Ejecuta la simulación
if __name__ == "__main__":
    #se le pasa la cantidad de filas y columnas, lo cual es el tamaño del array
    filas, columnas = 50, 50
    #se crea el tablero, especificando la probabilidad de vida
    tablero_inicial = crear_tablero(filas, columnas, prob_vida=0.2)
    #se pasan los datos del juego a la función para que inicie, especificando la cantidad de genraciones maximas y los intervalos
    simular_juego(tablero_inicial, generaciones_max=500, intervalo=100)

#endregion
