# Concesionario de coches
## Descripción de nuestro sistema de información

Deseamos crear un sistema de información que gestiona un concesionario de coches. Este sistema de información se dividirá en tres subsistemas: gestión de vehículos, lista de trabajadores y las ventas realizadas.

- En la **gestión de vehículos** tendremos en cuenta la marca, el modelo y la matrícula del coche y el subsistema se encargará de:
	- Encargar vehículo a proveedor
	- Anular encargo de vehículo
	- Comprobar fecha de entrega
	- Dar de alta un coche en el sistema
	- Dar de baja un coche en el sistema
	- Comprobar disponibilidad de un coches en el sistema  


- En la **lista de trabajadores** llevaremos un recuento del nombre, apellido, teléfono y el DNI de cada persona para identificarlos.
	- Consultar lista de trabajadores
	- Dar de alta un trabajador
	- Dar de baja un trabajador
	- Ver historial de ventas de un trabajador
	- Modificar datos de un trabajador  


- Por último, en las **ventas realizadas** almacenaremos el coche que ha sido vendido. Almacenaremos los datos del coche (Marca, modelo y matrícula), y también el DNI tanto del vendedor como del comprador.
	- Realizar una venta
	- Modificar una venta
	- Anular una venta
	- Ver historial de ventas
	- Ver estado de una venta  


## Requisitos de datos

- ***RD1.1 Información de un vehículo:***
	- **Marca:** Cadena de hasta 15 caracteres no vacía
	- **Modelo:** Cadena de hasta 20 caracteres no vacía
	- **Matrícula:** Cadena de hasta 10 caracteres  no vacía


- ***RD1.2 Información de un vehículo almacenado:***
	- **Marca:** Cadena de hasta 15 caracteres no vacía
	- **Modelo:** Cadena de hasta 20 caracteres no vacía
	- **Matrícula:** Cadena de hasta 10 caracteres no vacía
	- **Disponibilidad:** enum{stock, agotado, reservado, encargado}


- ***RD1.3 Información de un vehículo a mostrar:***
  - **Marca:** Cadena de hasta 15 caracteres no vacía
  - **Modelo:** Cadena de hasta 20 caracteres no vacía
  - **Matrícula:** Cadena de hasta 10 caracteres no vacía
  - **Disponibilidad:** enum{stock, agotado, reservado, encargado}


- ***RD2.1 Información de un trabajador***
	- **Nombre:** Cadena de hasta 20 caracteres no vacía
	- **Apellido:** Cadena de hasta 20 caracteres no vacía
	- **DNI:** Cadena alfanumérica
	- **Horario:** Horas y días de servicio del trabajador
	- **Teléfono de contacto:** Cadena numérica
	- **Ventas realizadas:** Historial de ventas realizadas


- ***RD2.2 Información de un trabajador almacenado***
	- **Nombre:** Cadena de hasta 20 caracteres no vacía
	- **Apellido:** Cadena de hasta 20 caracteres no vacía
	- **DNI:** Cadena alfanumérica
	- **Horario:** Horas y días de servicio del trabajador
	- **Teléfono de contacto:** Cadena numérica
	- **Ventas realizadas:** Historial de ventas realizadas


- ***RD2.3 Información de un trabajador a mostrar***
  - **Nombre:** Cadena de hasta 20 caracteres no vacía
  - **Apellido:** Cadena de hasta 20 caracteres no vacía
  - **DNI:** Cadena alfanumérica
  - **Horario:** Horas y días de servicio del trabajador
  - **Teléfono de contacto:** Cadena numérica
  - **Ventas realizadas:** Historial de ventas realizadas


- ***RD3.1 Información de una venta***
	- **Matrícula:**
	- **Cliente:** Nombre del comprador
	- **Vendedor:** Nombre del trabajador que efectúa la venta
	- **Importe:**
	- **Fecha de venta:**
	- **Fecha de entrega:**


- ***RD3.2 Información de una venta almacenada***
  - **Matrícula:**
  - **Cliente:** Nombre del comprador  
  - **Vendedor:** Nombre del trabajador que efectúa la venta
  - **Importe:**
  - **Fecha de venta:**
  - **Fecha de entrega:**


- ***RD3.3 Información de una venta a mostrar***
  - **Matrícula:**
  - **Cliente:** Nombre del comprador  
  - **Vendedor:** Nombre del trabajador que efectúa la venta
  - **Importe:**
  - **Fecha de venta:**
  - **Fecha de entrega:**


- ***RD3.4 Información de una reserva***
	- **Matrícula:**
	- **Cliente:**
	- **Vendedor:** Nombre del trabajador que efectúa la reserva
	- **Fianza:**
	- **Fecha de reserva:**


- ***RD3.5 Información de una reserva almacenada***
  - **Matrícula:**
  - **Cliente:**
  - **Vendedor:** Nombre del trabajador que efectúa la reserva
  - **Fianza:**
  - **Fecha de reserva:**


- ***RD3.6 Información de una reserva a mostrar***
  - **Matrícula:**
  - **Cliente:**
  - **Vendedor:** Nombre del trabajador que efectúa la reserva
  - **Fianza:**
  - **Fecha de reserva:**


## Requisitos funcionales

- ***RF1.1 Encargar vehículo a proveedor***
	- **E:** RD1.1
	- **A/M:** RD1.2
	- **S:**  -


-	***RF1.2 Anular encargo de vehículo***
	- **E:** RD1.1
	- **A/M:** RD1.2
	- **S:** -


- ***RF1.3 Dar de alta un vehículo***
  - **E:** RD1.1
  - **A/M:** RD1.2
  - **S:** -


- ***RF1.4 Dar de baja un vehículo***
  - **E:** RD1.1
  - **A/M:** RD1.2
  - **S:** -


- ***RF1.5 Comprobar disponibilidad de un vehículo***
  - **E:** RD1.1
  - **A/M:** RD1.2
  - **S:** RD1.3

- ***RF1.6 Comprobar vehículos disponibles***
  - **E:** RD1.1
  - **A/M:** RD1.2
  - **S:** RD1.3


- ***RF2.1 Consultar lista de trabajadores***
  - **E:** RD2.1
  - **A/M:** RD2.2
  - **S:** RD2.3


- ***RF2.2 Dar de alta un trabajador***
  - **E:** RD2.1
  - **A/M:** RD2.2
  - **S:** -


- ***RF2.3 Dar de baja un trabajador***
  - **E:** RD2.1
  - **A/M:** RD2.2
  - **S:** -


- ***RF2.4 Ver historial de ventas de un trabajador***
  - **E:** RD2.1
  - **A/M:** RD2.2
  - **S:** RD2.3


- ***RF2.5 Modificar datos de un trabajador***
  - **E:** RD2.1
  - **A/M:** RD2.2
  - **S:** -


- ***RF3.1 Realizar una venta***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** -


- ***RF3.2 Modificar una venta***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** -


- ***RF3.3 Anular una venta***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** -


- ***RF3.4 Ver historial de ventas***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** RD3.3


- ***RF3.5 Ver estado de la venta***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** RD3.3


- ***RF3.6 Comprobar fecha de entrega***
  - **E:** RD3.1
  - **A/M:** RD3.2
  - **S:** RD3.3



## Requisitos Semánticos

RS1.1: Dos vehículos no pueden tener la misma matrícula
RF1.3,RD1.2

RS2.1 Dos trabajadores no pueden vender el mismo vehículo
RF3.1,RD1.2

RS2.2 Dos trabajadores no pueden tener el mismo DNI
RF2.2,RD2.2

RS3.1: Un vehículo no puede ser vendido a dos clientes
RF3.1,RD3.3

RS3.2: No se puede realizar una venta de un vehículo que no esté en stock
TF3.1,RD1.2
