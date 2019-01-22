**Índice**   
1. [Introducción](#id1)
2. [Requisito de Datos](#id2)
3. [Requisitos Funcionales](#id3)
4. [Requisitos Semánticos](#id4)
5. [Practica 2](#id5)
	1. [Esquema caja negra](#id6)
	2. [Esquema armazón](#id7)
	3. [Refinamientos de cada subsistema](#id7)
	4. [Esquemas externos de procesos](#id8)
	5. [Diagrama de Entidad Relación del sistema](#id9)


## Introducción<a name="id1"></a>
Deseamos crear un sistema de información que gestiona un concesionario de coches. Este sistema de información se dividirá en tres subsistemas: gestión de vehículos, lista de trabajadores y ventas realizadas.

- En la **gestión de vehículos** tendremos en cuenta la marca, el modelo, el precio y la matrícula del coche, y el subsistema se encargará de:
	- Encargar vehículo a proveedor
	- Anular encargo de vehículo
	- Comprobar vehículos disponibles
	- Dar de alta un vehículo en el sistema
	- Dar de baja un vehículo en el sistema
	- Comprobar disponibilidad de un vehículo


- En la **lista de trabajadores** llevaremos un recuento del nombre, apellido, teléfono y DNI de cada persona para identificarlos.
	- Consultar lista de trabajadores
	- Dar de alta un trabajador
	- Dar de baja un trabajador
	- Ver historial de ventas de un trabajador
	- Modificar datos de un trabajador  


- Por último, en las **ventas realizadas** almacenaremos el vehículo que ha sido vendido. Almacenaremos los datos del coche (marca, modelo y matrícula), y también el DNI tanto del vendedor como del comprador.
	- Realizar una venta o reserva
	- Modificar una venta o reserva
	- Anular una venta o reserva
	- Ver historial de ventas y reservas
	- Ver estado de una venta
	- Comprobar fecha de entrega



## Requisitos de datos<a name="id2"></a>

- ***RD1.1 Datos de entrada para encargar vehículo a proveedor:***
	- **Id. Administrador:** Cadena de hasta 15 caracteres no vacía
	- **Id. Proveedor:** Cadena de hasta 15 caracteres no vacía
	- **Modelo:** Cadena de hasta 20 caracteres no vacía


- ***RD1.2 Datos de entrada para anular encargo de vehículo:***
- **Id. Administrador:** Cadena de hasta 15 caracteres no vacía
- **Id. Proveedor:** Cadena de hasta 20 caracteres no vacía
- **Modelo:** Cadena de hasta 20 caracteres no vacía


- ***RD1.3 Datos de entrada para dar de alta un vehículo:***
	- **Marca:** Cadena de hasta 15 caracteres no vacía
	- **Modelo:** Cadena de hasta 20 caracteres no vacía
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Precio:** Tipo numérico con dos cifras decimales


- ***RD1.4 Datos de entrada para dar de baja un vehículo:***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía


- ***RD1.5 Datos de entrada para comprobar disponibilidad de un vehículo:***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía


- ***RD1.6 Datos de entrada para comprobar vehículos disponibles:***
	- **Disponibilidad- stock:** Aquellos vehículos que estén en stock


- ***RD1.7 Información de un vehículo almacenado:***
	- **Marca:** Cadena de hasta 15 caracteres
	- **Modelo:** Cadena de hasta 20 caracteres no vacía
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Disponibilidad:** enum{stock, agotado, reservado, encargado}
	- **Precio:** Tipo numérico con dos cifras decimales


- ***RD1.8 Datos de salida para mostrar la disponibilidad de un vehículo:***
  - **Marca:** Cadena de hasta 15 caracteres no vacía
  - **Modelo:** Cadena de hasta 20 caracteres no vacía
  - **Matrícula:** Cadena de hasta 10 caracteres no vacía
  - **Disponibilidad:** enum{stock, agotado, reservado, encargado}
  - **Precio:** Tipo numérico con dos cifras decimales


- ***RD1.9 Datos de salida para mostrar vehículos disponibles:***
  - **Marca:** Cadena de hasta 15 caracteres no vacía
  - **Modelo:** Cadena de hasta 20 caracteres no vacía
  - **Matrícula:** Cadena de hasta 10 caracteres no vacía
  - **Disponibilidad:** enum{stock, agotado, reservado, encargado}
  - **Precio:** Tipo numérico con dos cifras decimales


- ***RD2.1 Datos de entrada para consultar lista de trabajadores***
	- **Nombre:** Cadena de hasta 50 caracteres no vacía
	- **DNI:** Cadena alfanumérica
	- **Horario:** Horas y días de servicio del trabajador
	- **Teléfono de contacto:** Cadena numérica
	- **Ventas realizadas:** Historial de ventas realizadas  


- ***RD2.2 Datos de entrada para dar de alta un trabajador***
	- **Nombre:** Cadena de hasta 50 caracteres no vacía
	- **DNI:** Cadena alfanumérica
	- **Horario:** Horas y días de servicio del trabajador
	- **Teléfono de contacto:** Cadena numérica
	- **Ventas realizadas:** Historial de ventas realizadas


- ***RD2.3 Datos de entrada para dar de baja un trabajador***
	- **DNI:** Cadena alfanumérica


- ***RD2.4 Datos de entrada para ver historial de ventas de un trabajador***
	- **DNI:** Cadena alfanumérica


- ***RD2.5 Datos de entrada para modificar datos de un trabajador***
	- **DNI:** Cadena alfanumérica


- ***RD2.6 Información de un trabajador almacenado***
	- **Nombre:** Cadena de hasta 50 caracteres no vacía
	- **DNI:** Cadena alfanumérica
	- **Horario:** Horas y días de servicio del trabajador
	- **Teléfono de contacto:** Cadena numérica
	- **Ventas realizadas:** Historial de ventas realizadas


- ***RD2.7 Datos de salida para consultar lista de trabajadores***
  - **Nombre:** Cadena de hasta 50 caracteres no vacía
  - **DNI:** Cadena alfanumérica
  - **Horario:** Horas y días de servicio del trabajador
  - **Teléfono de contacto:** Cadena numérica
  - **Ventas realizadas:** Historial de ventas realizadas


- ***RD2.8 Datos de salida para ver historial de ventas de un trabajador***
  - **Nombre:** Cadena de hasta 50 caracteres no vacía
  - **DNI:** Cadena alfanumérica
  - **Horario:** Horas y días de servicio del trabajador
  - **Teléfono de contacto:** Cadena numérica
  - **Ventas realizadas:** Historial de ventas realizadas


- ***RD3.1 Datos de entrada para realizar una venta***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
	- **DNI cliente:** Cadena alfanumérica
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Importe:** Precio del vehículo
	- **Fecha de venta:** Tipo date dd/mm/yyyy
	- **Fecha de entrega:** Tipo date dd/mm/yyyy
	- **Id. Venta:** Cadena de hasta 15 caracteres no vacía



- ***RD3.2 Datos de entrada para modificar una venta***
	- **Id. Venta:** Cadena de hasta 15 caracteres no vacía


- ***RD3.3 Datos de entrada para anular una venta***
	- **Id. Venta:** Cadena de hasta 15 caracteres no vacía


- ***RD3.4 Datos de entrada para ver historial de ventas***
	- **Fecha inicial:** Tipo date dd/mm/yyyy
	- **Fecha final:** Tipo date dd/mm/yyyy


- ***RD3.5 Datos de entrada para ver estado de la venta***
	- **Id. Venta:** Cadena de hasta 15 caracteres no vacía


- ***RD3.6 Datos de entrada para ver fecha de entrega***
	- **Id. Venta:** Cadena de hasta 15 caracteres no vacía



- ***RD3.7 Información de una venta almacenada***
  - **Matrícula:** Cadena de hasta 10 caracteres  no vacía
  - **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
  - **DNI cliente:** Cadena alfanumérica
  - **Vendedor:** Nombre del trabajador que efectúa la venta
  - **Importe:** Precio del vehículo
  - **Fecha de venta:** Tipo date dd/mm/yyyy
  - **Fecha de entrega:** Tipo date dd/mm/yyyy


- ***RD3.8 Información de una reserva almacenada***
  - **Matrícula:** Cadena de hasta 10 caracteres  no vacía
  - **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
  - **DNI cliente:** Cadena alfanumérica
  - **Vendedor:** Nombre del trabajador que efectúa la reserva
  - **Fianza:** Cantidad a pagar por adelantado
  - **Fecha de reserva:**  Tipo date dd/mm/yyyy
	- **Id. Reserva:** Cadena de hasta 15 caracteres no vacía



- ***RD3.9 Datos de entrada para realizar una reserva***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
	- **DNI cliente:** Cadena alfanumérica
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Fianza:** Cantidad a pagar por adelantado
	- **Fecha de reserva:**  Tipo date dd/mm/yyyy
	- **Id. Reserva:** Cadena de hasta 15 caracteres no vacía


- ***RD3.10 Datos de entrada para modificar una reserva***
	- **Id. Reserva:** Cadena de hasta 15 caracteres no vacía


- ***RD3.11 Datos de entrada para anular una reserva***
	- **Id. Reserva:** Cadena de hasta 15 caracteres no vacía


- ***RD3.12 Datos de entrada para ver historial de reservas***
	- **Fecha inicial:** Tipo date dd/mm/yyyy
	- **Fecha final:** Tipo date dd/mm/yyyy


- ***RD3.13 Datos de salida para ver historial de ventas***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
	- **DNI cliente:** Cadena alfanumérica
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Importe:** Precio del vehículo
	- **Fecha de venta:** Tipo date dd/mm/yyyy
	- **Fecha de entrega:** Tipo date dd/mm/yyyy



- ***RD3.14 Datos de salida para ver estado de la venta***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
	- **DNI cliente:** Cadena alfanumérica
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Importe:** Precio del vehículo
	- **Fecha de venta:** Tipo date dd/mm/yyyy
	- **Fecha de entrega:** Tipo date dd/mm/yyyy


- ***RD3.15 Datos de salida para comprobar fecha de entrega***
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía
	- **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
	- **DNI cliente:** Cadena alfanumérica
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Importe:** Precio del vehículo
	- **Fecha de venta:** Tipo date dd/mm/yyyy
	- **Fecha de entrega:** Tipo date dd/mm/yyyy


- ***RD3.16 Datos de salida para ver historial de reservas***
  - **Matrícula:** Cadena de hasta 10 caracteres  no vacía
  - **Nombre cliente:** Cadena de hasta 40 caracteres  no vacía
  - **DNI cliente:** Cadena alfanumérica
  - **Vendedor:** Nombre del trabajador que efectúa la reserva
  - **Fianza:** Cantidad a pagar por adelantado
  - **Fecha de reserva:** Tipo date dd/mm/yyyy


## Requisitos funcionales<a name="id3"></a>


- ***RF1.1 Encargar vehículo a proveedor***
	- **E:** RD1.1
	- **A/M:** RD1.7
	- **S:**  -


-	***RF1.2 Anular encargo de vehículo***
	- **E:** RD1.2
	- **A/M:** RD1.7
	- **S:** -


- ***RF1.3 Dar de alta un vehículo***
  - **E:** RD1.3
  - **A/M:** RD1.7
  - **S:** -


- ***RF1.4 Dar de baja un vehículo***
  - **E:** RD1.4
  - **A/M:** RD1.7
  - **S:** -


- ***RF1.5 Comprobar disponibilidad de un vehículo***
  - **E:** RD1.5
  - **A/M:** RD1.7
  - **S:** RD1.8


- ***RF1.6 Comprobar vehículos disponibles***
  - **E:** RD1.6
  - **A/M:** RD1.7
  - **S:** RD1.9


- ***RF2.1 Consultar lista de trabajadores***
  - **E:** RD2.1
  - **A/M:** RD2.6
  - **S:** RD2.7


- ***RF2.2 Dar de alta un trabajador***
  - **E:** RD2.2
  - **A/M:** RD2.6
  - **S:** -


- ***RF2.3 Dar de baja un trabajador***
  - **E:** RD2.3
  - **A/M:** RD2.6
  - **S:** -


- ***RF2.4 Ver historial de ventas de un trabajador***
  - **E:** RD2.4
  - **A/M:** RD2.6
  - **S:** RD2.8


- ***RF2.5 Modificar datos de un trabajador***
  - **E:** RD2.5
  - **A/M:** RD2.6
  - **S:** -


- ***RF3.1 Realizar una venta***
  - **E:** RD3.1
  - **A/M:** RD3.7
  - **S:** -


- ***RF3.2 Modificar una venta***
  - **E:** RD3.2
  - **A/M:** RD3.7
  - **S:** -


- ***RF3.3 Anular una venta***
  - **E:** RD3.3
  - **A/M:** RD3.7
  - **S:** -


- ***RF3.4 Ver historial de ventas***
  - **E:** RD3.4
  - **A/M:** RD3.7
  - **S:** RD3.13


- ***RF3.5 Ver estado de la venta***
  - **E:** RD3.5
  - **A/M:** RD3.7
  - **S:** RD3.14


- ***RF3.6 Comprobar fecha de entrega***
  - **E:** RD3.6
  - **A/M:** RD3.7
  - **S:** RD3.15


- ***RF3.7 Realizar una reserva***
  - **E:** RD3.9
  - **A/M:** RD3.8
  - **S:** -


- ***RF3.8 Modificar una reserva***
  - **E:** RD3.10
  - **A/M:** RD3.8
  - **S:** -


- ***RF3.9 Anular una reserva***
  - **E:** RD3.11
  - **A/M:** RD3.8
  - **S:** -


- ***RF3.10 Ver historial de reservas***
  - **E:** RD3.12
  - **A/M:** RD3.8
  - **S:** RD3.16



## Requisitos semánticos <a name="id4"></a>
- ***RS1.1: Dos vehículos no pueden tener la misma matrícula***
 - **RF1.3,RD1.7**


- ***RS2.1: Dos trabajadores no pueden vender el mismo vehículo***
	- **RF3.1,RD3.7**


- ***RS2.2: Dos trabajadores no pueden tener el mismo DNI***
	- **RF2.2,RD2.6**


- ***RS3.1: Un vehículo no puede ser vendido a dos clientes distintos***
	- **RF3.1,RD3.7**


- ***RS3.2: Un vehículo no puede ser reservado por dos clientes distintos***
	- **RF3.7,RD3.8**


- ***RS3.2: No se puede realizar una venta de un vehículo que no esté en stock***
	- **RF3.1,RD1.7**
