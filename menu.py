catalogo=[]
def agregar_producto():
    while True:
        print("1. Peliculas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos Deportivos")
        agregar_producto = input("Seleciona una categoria, donde desees agregar el producto, o selecciona 0 para terminar:").lower()
        if agregar_producto == "peliculas":
            agregar_pelicula()
        elif agregar_producto == "series":
            agregar_serie()
        elif agregar_producto == "documentales":
            agregar_documental()
        elif agregar_producto == "eventos deportivos":
            agregar_evento_deportivo()
        elif agregar_producto == "0":
            break
        else:
            print("opciopn invalida, selecione entre peliculas, series, documentales, eventos deportivos ")
def agregar_pelicula():
    caracteristicas = input("Ingrese la película:\n"
                   "recuerde ingresarlo: Título, actriz o actor principal, directora o director, año. ")
    catalogo.append({"Tipo": "Película","Titulo": caracteristicas})
    print("La película se ha agregado.")
def agregar_serie():
    caracteristicas = input("Ingrese la serie:\n"
                   "recuerde ingresarlo: Título, actriz o actor principal, directora o director, temporadas. ")
    catalogo.append({"Tipo": "Serie","Titulo": caracteristicas})
    print("La película se ha agregado.")
def agregar_documental():
    caracteristicas = input("Ingrese el título del documental:\n"
                   "recuerde ingresarlo: Título, director o directora, tema, año. ")
    catalogo.append({"Tipo": "Documentales", "Titulo": caracteristicas})
def agregar_evento_deportivo():
    caracteristicas = input("Ingrese un evento deportivo:\n"
                   "recuerde ingresarlo: Título, deporte, fecha, hora, lugar.")
    catalogo.append({"Tipo": "Evento Deportivo", "Titulo": caracteristicas})

def buscar_producto():
    print("recuerda primero cargar un archivo")
    clave = input("Ingrese palabra clave: ")
    resultados = []

    for producto in catalogo:
        if clave.lower() in producto["Título"].lower():
            resultados.append(producto)

    if len(resultados) > 0:
        print(f"Se encontraron {len(resultados)} resultado(s) que coinciden con la búsqueda:")
        for producto in resultados:
            print(f"Tipo: {producto['Tipo']}")
            print(f"Título: {producto['Título']}")
    else:
        print("No se encontraron productos con la búsqueda.")

def eliminar_producto():
    titulo = input("Ingrese el título del producto que desea eliminar: ")

    for producto in catalogo:
        if producto["Título"] == titulo:
            catalogo.remove(producto)
            print("El producto fue eliminado.")
            return

    print("No se encontró producto.")
def mostrar_catalogo():
    while True:
        print("Catalogo")
        print("1. Peliculas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos Deportivos")
        print("5. Todo")
        print("6. Regresar")
        opcion = input("Selecciona una opcion de las anteriores:").lower()

        import ast

        # Abre el archivo en modo lectura
        with open("catalogo_principal.txt", "r") as archivo:
            contenido = archivo.read()

        # Convierte el contenido del archivo en una lista de diccionarios
        lista_elementos = ast.literal_eval(contenido)

        if opcion == "peliculas":
            for elemento in lista_elementos:
                if elemento['Tipo'] == 'Película':
                    print(elemento)

        elif opcion == "series":
            for elemento in lista_elementos:
                if elemento['Tipo'] == 'Serie':
                    print(elemento)

        elif opcion == "documentales":
            for elemento in lista_elementos:
                if elemento['Tipo'] == 'Documentales':
                    print(elemento)


        elif opcion == "eventos deportivos":
            for elemento in lista_elementos:
                if elemento['Tipo'] == 'Evento Deportivo':
                    print(elemento)

        elif opcion == "todo":
            with open("catalogo_principal.txt", "r") as archivo:
                contenido = archivo.read()
            lista_datos = eval(contenido)
            for elemento in lista_datos:
                tipo = elemento.get('Tipo')
                if tipo is not None:
                    print("Elemento de tipo:", tipo)
                    print(elemento)
                    print()



        elif opcion == 6:
            print("saliendo del catalogo")
            print("regresando al menu principal")
            break
        else:
            print("Opcion invalida, por favor selcciona una opcion valida (peliculas, series, documentales, eventos deportivos, todo) ")

