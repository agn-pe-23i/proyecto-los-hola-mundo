[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
# Descripción del proyecto:



Un servicio de streaming requiere actualizar su sistema de renta y venta de películas, series, documentales y eventos deportivos en vivo. Para esto, es necesario contar con un catálogo de los productos con los que cuenta y transmitirá. El sistema deberá permitir interactuar con el catálogo a través de una serie de menús que faciliten la manipulación correcta y completa del catálogo de productos. El objetivo del sistema es facilitar dicha tarea, por lo que emplea temas vistos en la UEA de “Programación estructurada”

El script deberá ser intuitivo para el usuario por lo que se debe llevar un orden, para lograr dicho objetivo se deberá hacer de primera mano el diagrama de estructura, para después emplearlo en el script, el diagrama facilitará la elaboración de esta práctica


# Diagrama de Estructra:

![fig1](https://github.com/agn-pe-23i/proyecto-los-hola-mundo/assets/125332082/626d9bac-a8ec-4186-b558-c130e904eea0)

(fig1 Diagrama de estructura)


El diagrama de estructura vista en la figura anterior fue la base de cómo se haría el script. Se puede apreciar que el menú principal siempre recibirá la información de 1 de los 7 funciones dependiendo de la elección del usuario. La información que proporciona el usuario es un valor numérico (int) entre 1 al 7 que son las opciones del menú y al interactuar con el módulo da una salida en forma de (str).


# Correspondencia entre el diseño y la implementación 


Una vez que ya mencionamos como está diseñado el diagrama de estructura lo vamos a emplear para crear los scripts, el script principal será “Menú principal” el cual recibirá información de tipo numérico (int) entre el 1 al 7, donde este último es la opción de salir que básicamente termina el programa. 
En cuanto a los otros seis, son scripts de forma independiente pero que dan una salida de tipo (str), estos empezaran a funcionar cuando el usuario lo requiera, también llamados módulos mencionare el uso del 1 al 6.

De igual manera en el siguiente apartdo se habla con más detalle de la implementación.



# Comentarios del diseño de implementación y Documentación

*Menú principal:*

Objetivo: Este menú considera las siguientes opciones.
  Menú principal

  
   1-Agregar un producto
   
   2-Buscar producto
   
   3-Eliminar un producto
   
   4-Mostrar el catálogo
   
   5- Cargar catálogo
   
   6-Guardar catálogo
   
   7-Salir


Para poder implementar esta solución en Python comenzamos con la estructura del diagrama y el menú es quien desplegará la elección solicitada. Al ser el menú principal es quien va a tener todos los módulos (mostradas en el diagrama de estructura).


*Agregar producto:*

Objetivo:Para cada opción, el sistema debe solicitar y recibir correctamente la información correspondiente, validando los valores ingresados y resolviendo los posibles errores que existan durante la ejecución del sistema.

Menú agregar producto

  1-Película
  
  2- Series
  
  3-Documental
  
  4-Evento deportivo en vivo
  
  5-Regresar

En el menú principal, cuando se dé la opción de “agregar producto” el programa mostrará las diferentes categorías existentes donde se desee agregar el producto.


*Buscar producto:*

Objetivo: El sistema debe solicitar palabras clave del título del producto a buscar y desplegar todos los productos que coincidan con el criterio de búsqueda, mostrando también el tipo de producto que son.

Con el archivo de texto que creamos para películas, series, eventos deportivos y documentales. Lo que debemos hacer es que el programa solicite al usuario escribir cualquier número y/o letra y nuestro programa deberá buscar en el archivo de texto (.txt) algún elemento relacionado.

*Eliminar producto:*

Objetivo: Para eliminar un producto, es necesario que el usuario introduzca la información necesaria para identificar de forma única el producto que desea eliminar
Para eliminar un producto debemos buscar el elemento en los archivos.

 Para eliminar un producto debemos buscar el elemento en el archivo de texto. En nuestro caso, para ser específicos, debemos seleccionar la categoría en donde se encuentra el producto e introducir el mismo con todos sus datos, es decir, su nombre, autor, año. Según sea el caso. Una vez hecho esto, se mandará un mensaje de que el producto ha sido eliminado, o en su defecto, mostrará que no se encontró dicho producto. 


*Mostrar catálogo:*

Objetivo: Esta opción desplegará el siguiente menú secundario y mostrará, de forma ordenada, la información de los productos de acuerdo con la elección del usuario.

Menú mostrar catálogo

  1-Películas
  
  2- series
  
  3-Documentales
  
  4-Eventos deportivos
  
  5-Todo
  
  6-Regresar

Si en el menú principal se da la opción de “Mostrar catálogo” este a su vez mostrará un menú secundario (como se puede apreciar en el ejemplo) y una vez que se elija una de las seis opciones. Dependiendo de que se haya seleccionado, desplegará lo que haya en archivo de texto, y en caso de que se seleccione la opción “Todo” mostrará todas las categorías del catálogo.


*Cargar catálogo:*

Objetivo: El sistema solicitará el nombre del archivo en donde está almacenado el catálogo. Si el archivo existe y se puede leer, se cargará el contenido del mismo.




*Guardar catálogo:*

Objetivo: El sistema solicitará el nombre del archivo en donde se guardará el catálogo. Si el archivo se puede abrir para escritura, se guardarán los datos de los productos.

