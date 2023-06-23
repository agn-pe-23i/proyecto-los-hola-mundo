[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
# Descripción del proyecto:


Un servicio de streaming requiere actualizar su sistema de renta y venta de películas, series, documentales y eventos deportivos en vivo. Para esto, es necesario contar con un catálogo de los productos con los que cuenta y transmitirá. El sistema deberá permitir interactuar con el catálogo a través de una serie de menús que faciliten la manipulación correcta y completa del catálogo de productos. El objetivo del sistema es facilitar dicha tarea, por lo que emplea temas vistos en la UEA de “Programación estructurada”

El script deberá ser intuitivo para el usuario por lo que se debe llevar un orden, por lo que se deberá hacer de primera mano el diagrama de estructura, para después emplearlo en el script, el diagrama facilitará la elaboración de esta práctica


# Diagrama de Estructra:
![diagrama_estructura](https://github.com/agn-pe-23i/proyecto-los-hola-mundo/assets/125332082/93012716-2db9-4f64-911b-52512a901269)
(fig1 Diagrama de estructura)

El diagrama de estructura vista en la figura anterior, (fig1) fue la base de cómo se haría el script. Se puede apreciar que el menú principal siempre recibirá la información de 1 de los 7 módulos dependiendo de la elección del usuario. La información que proporciona el usuario es un valor numérico (int) entre 1 al 7 que son las opciones del menú y al interactuar con el módulo da una salida en forma de (str).


# Correspondencia entre el diseño y la implementación 


Una vez que ya mencionamos como está diseñado el diagrama de estructura lo vamos a emplear para crear los scripts, el script principal será “Menú principal” el cual recibirá información de tipo numérico (int) entre el 1 al 7, donde este último es la opción de salir que básicamente termina el programa. 
En cuanto a los otros seis, son scripts de forma independiente pero que dan una salida de tipo (str), estos empezaran a funcionar cuando el usuario lo requiera, también llamados módulos mencionare el uso del 1 al 6.



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

