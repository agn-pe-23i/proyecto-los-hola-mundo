#Importamos  el catalogo
import menu
#Hacemos una funcion para cargar catalago donde va a leer el archivo.txt
def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            menu.catalogo_productos = eval(archivo.read())
        print("El catálogo se ha cargado.")
    except FileNotFoundError:
        print("catalogo no existe.")
    except:
        print("Ocurrió un error.")
def guardar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(str(menu.catalogo))
        print("Se ha guardado correctamente.")
    except:
        print("Ocurrió un error.")
