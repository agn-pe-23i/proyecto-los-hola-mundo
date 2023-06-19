[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Reporte del Proyecto Final
•-----------------------------•
|   menú_principal        |
•-----------------------------•
                |
                |
                |           •-----------------------------•
                •----------|   agregar_producto   |
                |           •-----------------------------•
                |
                |
                |            •---------------------------•
                •-----------|  buscar_producto   |
                |            •---------------------------•
                |
                |
                |            •-----------------------------•
                •-----------|   eliminar_producto |
                |            •-----------------------------•
                |
                |
                |           •----------------------------•               •---------------•
                •----------|   mostrar_catálogo             |-------------|   películas | 
                |           •----------------------------•               •---------------•
                |                                                                         |
                |                                                                         |
                |            •--------------------------•                                 |
                •-----------|cargar_catálogo     |                             •---------------•
                             •--------------------------•                      | Series       |
                                                                                •---------------•   
                                                                                          |
                                                                                          |
                                                                                 •--------------------•
                                                                                 |Documentales |
                                                                                 •--------------------•
                                                                                           |
                                                                                           |
                                                                                           |
                                                                                  •--------------------------•          
                                                                                  | eventos_deportivos|
                                                                                  •--------------------------•
                                                                                            | 
                                                                                            |
                                                                                    •-----------•
                                                                                     |   todo   |      
                                                                                     •-----------•
Para iniciar con el desarrollo de la práctica creamos el diagrama de estructura, como tomamos de referencia una plataforma de streaming nos basamos en los menús y cómo estos despliegan acciones o información. Posterior a eso cada opción tendrá una tarea muy específica que ayudará al funcionamiento del script. 
Una vez que ya tenemos el diagrama de estructura  de como va estar dividido hacemos un script por cada opción.
Menú principal:
Objetivo: Este menú considera las siguientes opciones.
Menú principal
Agregar un producto
Buscar producto
Eliminar un producto
Mostrar el catálogo
Cargar catálogo
Guardar catálogo
Salir
Para poder implementar esta solución en Python iniciamos con la estructura del diagrama y el menú es quien desplegará la elección solicitada. Al ser el menú principal es quien va tener todos los módulos (mostradas en el diagrama de estructura)
Agregar producto:
Objetivo:Para cada opción, el sistema debe solicitar y recibir correctamente la información correspondiente, validando los valores ingresados y resolviendo los posibles errores que existan durante la ejecución del sistema.
Menú agregar producto
Película
Serie
Documental
Evento deportivo en vivo
Regresar
En el menú principal cuando se dé la opción de “agregar producto” el programa mostrará las diferentes categorías existentes donde se desee agregar el producto.
Buscar producto:
Objetivo: El sistema debe solicitar palabras clave del título del producto a buscar y desplegar todos los productos que coincidan con el criterio de búsqueda, mostrando también el tipo de producto que son.
Con los archivos de texto que creamos para los diferentes catálogos, películas, series, eventos deportivos y documentales lo que debemos hacer es que el programa solicite al usuario escribir cualquier número y/o letra y nuestro programa deberá buscar en los archivos de texto (.txt) algún elemento relacionado.
Eliminar producto:
Objetivo: Para eliminar un producto, es necesario que el usuario introduzca la información necesaria para identificar de forma única el producto que desea eliminar
Para eliminar un producto debemos buscar el elemento en los archivos. En nuestro caso para ser específicos, debemos seleccionar la categoría en donde se encuentra el producto e introducir el mismo con todos sus datos, es decir, su nombre, autor, año. Según sea el caso. Una vez hecho esto se mandará un mensaje de que el producto ha sido eliminado, o en su defecto, mostrará que no se encontró dicho producto. 
Mostrar catálogo:
Objetivo: Esta opción desplegará el siguiente menú secundario y mostrará, de forma ordenada, la información de los productos de acuerdo con la elección del usuario.
Menú mostrar catálogo
Películas
Series
Documentales
Eventos deportivos
Todo
Regresar
Si en el menú principal se da la opción de “Mostrar catálogo” este a su vez mostrará un menú secundario (como se puede apreciar en el ejemplo) y una vez que se elija una de las seis opciones. Dependiendo de que se haya seleccionado desplegará lo que haya en archivo de texto, y en caso de que se seleccione la opción “Todo” mostrará todos los elementos de los archivos de texto.

Cargar catálogo:
Objetivo: El sistema solicitará el nombre del archivo en donde está almacenado el catálogo. Si el archivo existe y se puede leer, se cargará el contenido del mismo.
Cuando el usuario elija la opción de cargar catálogo, el usuario deberá escribir el nombre de un archivo de texto ya existente. Posteriormente, cargará los productos del catálogo seleccionado.


Guardar catálogo:
Objetivo: El sistema solicitará el nombre del archivo en donde se guardará el catálogo. Si el archivo se puede abrir para escritura, se guardarán los datos de los productos.
Esta última opción le pedirá al usuario que escriba el nombre de un archivo de texto existente, en el cual guardará el producto deseado.
