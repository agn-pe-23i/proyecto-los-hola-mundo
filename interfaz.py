import menu
import catalogo
#Se hace la funcion menu principal
def menu_principal():
    print("Menú principal")
    print("1. Agregar un producto")
    print("2. Buscar producto")
    print("3. Eliminar un producto")
    print("4. Mostrar el catálogo")
    print("5. Cargar catálogo")
    print("6. Guardar catálogo")
    print("7. Salir")

    opcion = input("Porfavor haga una seleccion: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "1":
        menu.agregar_producto()
    elif opcion == "2":
        menu.buscar_producto()
    elif opcion == "3":
        menu.eliminar_producto()
    elif opcion == "4":
        menu.mostrar_catalogo()
    elif opcion == "5":
        catalogo.cargar_catalogo()
    elif opcion == "6":
        catalogo.guardar_catalogo()
    elif opcion == "7":
        print("Adios")
    else:
        print("Seleccione una opcion valida.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "7":
            break
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
