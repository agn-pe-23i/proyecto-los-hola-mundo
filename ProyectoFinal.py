def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar un producto")
        print("2. Buscar un producto")
        print("3. Eliminar un producto")
        print("4. Mostrar catálogo")
        print("5. Cargar catálogo")
        print("6. Guardar catálogo")
        print("7. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            mostrar_catalogo()
        elif opcion == "5":
            cargar_catalogo()
        elif opcion == "6":
            guardar_catalogo()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 7.")
# Función para agregar un producto al catálogo
def agregar_producto():
    while True:
        print("1. Peliculas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos Deportivos")
        agregar_producto = int(input("Seleciona una categoria, donde desees agregar el producto, o selecciona 0 para terminar:"))

        if agregar_producto == 1:
            archivo = open("catálogoPeliculas.txt", "a")
            while True:
                # Solicitar al usuario que ingrese el nombre de una película
                nombre_pelicula = input("Ingresa el nombre de una película (o escribe 'salir' para terminar): ")

                if nombre_pelicula.lower() == "salir":
                    break

                # Escribir el nombre de la película en el archivo
                archivo.write(nombre_pelicula + "\n")

            # Cerrar el archivo
            archivo.close()
        elif agregar_producto == 2:
            archivo = open("catálogoSeries.txt", "a")
            while True:
                # Solicitar al usuario que ingrese el nombre de una serie
                nombre_serie = input("Ingresa el nombre de una serie (o escribe 'salir' para terminar): ")

                if nombre_serie.lower() == "salir":
                    break

                # Escribir el nombre en el archivo
                archivo.write(nombre_serie + "\n")

            # Cerrar el archivo
            archivo.close()
        elif agregar_producto == 3:
            archivo = open("catálogoDocumentales.txt", "a")
            while True:
                # Solicitar al usuario que ingrese el nombre de un documental
                nombre_documental = input("Ingresa el nombre de un Documental (o escribe 'salir' para terminar): ")

                if nombre_documental.lower() == "salir":
                    break

                # Escribir el nombre en el archivo
                archivo.write(nombre_documental + "\n")

            # Cerrar el archivo
            archivo.close()
        elif agregar_producto == 4:
            archivo = open("CatálogoEventosdeportivos.txt", "a")
            while True:
                # Solicitar al usuario que ingrese el nombre de un eventos deportivos
                nombre_evento_deportivo = input(
                    "Ingresa el nombre de un Evento deportivo (o escribe 'salir' para terminar): ")

                if nombre_evento_deportivo.lower() == "salir":
                    break

                # Escribir el nombre en el archivo
                archivo.write(nombre_evento_deportivo + "\n")

            # Cerrar el archivo
            archivo.close()
        elif agregar_producto == 0:
            print("Prodcutos guardados cobn exito.")

            break
        else:
            print("Opcion invalida, por seleccione una opcion del 0 al 4")


# Función para buscar un producto en el catálogodef buscar_producto():
def buscar_producto():
    def buscar_elemento_en_archivo(ruta_archivo, elemento):
        # Abre el archivo en modo lectura
        with open(ruta_archivo, 'r') as archivo:
            # Inicializa una lista para almacenar las líneas que contienen el elemento
            lineas_encontradas = []

            # Itera sobre cada línea del archivo
            for numero_linea, linea in enumerate(archivo, start=1):
                # Verifica si el elemento buscado está presente en la línea actual
                if elemento in linea:
                    # Guarda la línea completa en la lista
                    lineas_encontradas.append((numero_linea, linea.strip()))

        # Cierra el archivo

        # Retorna las líneas que contienen el elemento encontrado
        return lineas_encontradas

    # Función para buscar un elemento en varios archivos de texto
    def buscar_elemento_en_varios_archivos(rutas_archivos, elemento):
        for ruta_archivo in rutas_archivos:
            lineas_encontradas = buscar_elemento_en_archivo(ruta_archivo, elemento)
            if lineas_encontradas:
                print(f"El elemento '{elemento}' se encontró en el catálogo '{ruta_archivo}':")
                for numero_linea, linea in lineas_encontradas:
                    print(f"{linea}")
                print()

    rutas_archivos = ['catálogoPeliculas.txt', 'catálogoSeries.txt', 'catálogoDocumentales.txt',
                      'CatálogoEventosdeportivos.txt']
    elemento= input("Ingresa el nombre de la pelicula, serie, documental o evento que quieres buscar: ")
    elemento_buscado = elemento.lower()
    buscar_elemento_en_varios_archivos(rutas_archivos, elemento_buscado)


# Función para eliminar un producto del catálogo
def eliminar_producto():
    import os

    categorias = {
        "pelicula": "catálogoPeliculas.txt",
        "documental": "catálogodocumentales.txt",
        "evento deportivo": "CatalogoEventosDeportivos.txt",
        "serie": "catálogoSeries.txt"
    }

    def eliminar_renglon_categoria(categoria, texto_renglon):
        # Verificar si la categoría existe
        if categoria not in categorias:
            print("Categoría no válida.")
            return

        # Obtener el archivo asociado a la categoría
        nombre_archivo = categorias[categoria]

        # Verificar si el archivo existe
        if not os.path.isfile(nombre_archivo):
            print(f"No se encontró el archivo '{nombre_archivo}'.")
            return

        # Leer el contenido del archivo
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

        # Buscar el texto en cada renglón
        for i, linea in enumerate(lineas):
            if texto_renglon.lower() in linea:
                # Eliminar el renglón correspondiente
                lineas.pop(i)
                break
        else:
            print("El texto especificado no se encontró en el archivo.")
            return

        # Escribir el contenido actualizado en el archivo
        with open(nombre_archivo, "w") as archivo:
            archivo.writelines(lineas)

        print("El renglón ha sido eliminado con éxito.")

    categoria = input("Ingrese la categoría (pelicula, documental, evento deportivo, serie): ")
    texto_renglon = input("Ingrese ingrese el producto que desea eliminar: ")

    eliminar_renglon_categoria(categoria, texto_renglon)

# Función para mostrar el catálogo completo
def mostrar_catalogo():
    while True:
        print("Catalogo")
        print("1. Peliculas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos Deportivos")
        print("5. Todo")
        print("6. Regresar")
        opcion = int(input("Selecciona una opcion de las anteriores:"))
        if opcion == 1:
            # Paso 1: Abre el archivo en modo lectura
            archivo = open('catálogoPeliculas.txt', 'r')

            # Paso 2: Lee el contenido del archivo
            contenido = archivo.readlines()

            # Paso 3: Muestra los elementos del archivo
            for elemento in contenido:
                print(elemento)

            # Paso 4: Cierra el archivo
            archivo.close()

        elif opcion == 2:
            # Paso 1: Abre el archivo en modo lectura
            archivo = open('catálogoSeries.txt', 'r')

            # Paso 2: Lee el contenido del archivo
            contenido = archivo.readlines()

            # Paso 3: Muestra los elementos del archivo
            for elemento in contenido:
                print(elemento)

            # Paso 4: Cierra el archivo
            archivo.close()

        elif opcion == 3:
            # Paso 1: Abre el archivo en modo lectura
            archivo = open('catálogoDocumentales.txt', 'r')

            # Paso 2: Lee el contenido del archivo
            contenido = archivo.readlines()

            # Paso 3: Muestra los elementos del archivo
            for elemento in contenido:
                print(elemento)

            # Paso 4: Cierra el archivo
            archivo.close()

        elif opcion == 4:
            # Paso 1: Abre el archivo en modo lectura
            archivo = open('CatálogoEventosdeportivos.txt', 'r')

            # Paso 2: Lee el contenido del archivo
            contenido = archivo.readlines()

            # Paso 3: Muestra los elementos del archivo
            for elemento in contenido:
                print(elemento)

            # Paso 4: Cierra el archivo
            archivo.close()

        elif opcion == 5:
            # Lista de archivos
            archivos = ["catálogoPeliculas.txt", "catálogoSeries.txt", "catálogoDocumentales.txt",
                        "CatálogoEventosdeportivos.txt"]

            # Recorre cada archivo de la lista
            for archivo in archivos:
                # Paso 1: Abre el archivo en modo lectura
                archivo_actual = open(archivo, 'r')

                # Paso 2: Lee el contenido del archivo
                contenido = archivo_actual.readlines()

                # Paso 3: Muestra los elementos del archivo
                print(f"Elementos en {archivo}:")
                for elemento in contenido:
                    print(elemento)

                # Paso 4: Cierra el archivo
                archivo_actual.close()
        elif opcion == 6:
            print("saliendo del catalogo")
            print("regresando al menu principal")
            break
        else:
            print("Opcion invalida, por favor selcciona un numero del 1 al 6")
def cargar_catalogo():
    #En esta seccion le pediremos al usuario que escriba el nombre del archivo de texto que se desea cargar
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    #Una vez que se haya encontrado el archivo, se iniciará el modo lectura
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        #irá iterando linea por linea en el archivo de txto
        for linea in lineas:
            print(linea.strip())

def guardar_catalogo():
    #El usuario ingresará el nombre del archivo de texto
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    #En la sig linea se emplea una función para que se pueda agregar un elemnto al final del archivo de texto
    with open(nombre_archivo, "a") as archivo:
        while True:
            #En esta seccion le dará la opcion al usuario para escriba el elemto que desea fuaradr en el catálogo
            datos_nuevos = input("Ingrese los datos a agregar al archivo (ingrese 'salir' para finalizar): ")
            if datos_nuevos.lower() == "salir":
                break
            archivo.write(datos_nuevos + "\n")

menu_principal()
