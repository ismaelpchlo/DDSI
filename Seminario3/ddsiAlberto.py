# -*- coding: utf-8 -*-

#------------------------------------------------
# DATOS INICIALIZACIÓN
#------------------------------------------------

from datetime import date
import sqlite3
connection = sqlite3.connect("trabajadores.db")

cursor= connection.cursor()

#cursor.execute("""DROP TABLE Administrador;""")
#cursor.execute("""DROP TABLE Trabajador;""")
#cursor.execute("""DROP TABLE Vehiculo;""")
#cursor.execute("""DROP TABLE Proveedor;""")
#cursor.execute("""DROP TABLE Ventas;""")
#cursor.execute("""DROP TABLE Encargar;""")
#cursor.execute("""DROP TABLE Suministra;""")
#cursor.execute("""DROP TABLE Gestiona;""")
#cursor.execute("""DROP TABLE Reservas;""")
#cursor.execute("""DROP TABLE Gestiona1;""")
#cursor.execute("""DROP TABLE Gestiona2;""")
#cursor.execute("""DROP TABLE Realiza;""")

#------------------------------------------------
# CREACIÓN DE TABLAS
#------------------------------------------------

#Tabla Administrador
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Administrador'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Administrador',):
	sql_command="""
	CREATE TABLE Administrador(
		Identificador int PRIMARY KEY,
		Nombre_apellidos varchar(50) NOT NULL
	);"""
	cursor.execute(sql_command)
	print("Se ha creado la tabla Administrador")


# Tabla Trabajador
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Trabajador';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Trabajador',):
	sql_command="""
	CREATE TABLE Trabajador(
		DNI int PRIMARY KEY,
		Nombre_apellidos varchar(50) NOT NULL,
		Horario varchar(100),
		Telefono int,
		VentasRealizadas int
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Trabajador")



# Tabla Vehiculo
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Vehiculo';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Vehiculo',):
	sql_command="""
	CREATE TABLE Vehiculo(
		Matricula varchar(10) PRIMARY KEY,
		Marca varchar(15) NOT NULL,
		Modelo varchar(20),
		Disponibilidad varchar2(15) CHECK (Disponibilidad IN ('stock', 'agotado', 			'reservado', 'encargado')),
		Precio varchar(15)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Vehiculo")


# Tabla Proveedor
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Proveedor';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Proveedor',):
	sql_command="""
	CREATE TABLE Proveedor(
		IdentificadorP int PRIMARY KEY,
		Nombre_empresa varchar(50) NOT NULL
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Proveedor")



# Tabla Ventas
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Ventas';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Ventas',):
	sql_command="""
	CREATE TABLE Ventas(
	  	Identificador int,
		Matricula varchar(10) REFERENCES Vehiculo(Matricula),
	    DNI_cliente int,
	    Fecha_venta date,
	    PRIMARY KEY(Identificador)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Ventas")





#Tabla Encargar
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Encargar'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Encargar',):
	sql_command="""
	CREATE TABLE Encargar(
		Identificador int REFERENCES Administrador(Identificador),
		IdentificadorP int REFERENCES Proveedor(IdentificadorP),
		Matricula varchar(10) REFERENCES Vehiculo(Matricula),
		Fecha DATE,
		PRIMARY KEY( Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Encargar")


#Tabla Suministra
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Suministra'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Suministra',):
	sql_command="""
	CREATE TABLE Suministra(
		IdentificadorP int REFERENCES Proveedor(IdentificadorP),
		Matricula varchar(10) REFERENCES Vehiculo(Matricula),
		PRIMARY KEY( Matricula)
	);
	"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Suministra")


#Tabla Gestiona
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Gestiona'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Gestiona',):
	sql_command="""
	CREATE TABLE Gestiona(
		Identificador int REFERENCES Administrador(Identificador),
		Matricula varchar(10) REFERENCES Vehiculo(Matricula),
		PRIMARY KEY( Identificador, Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Gestiona")




#Tabla Reservas
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Reservas'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Reservas',):
	sql_command="""
	CREATE TABLE Reservas(
	  	Identificador int,
	    	Matricula varchar(10),
	    	DNI_cliente int,
	    	Fecha_realizada date,
	    	Fecha_entrega date,
	    	PRIMARY KEY(Identificador)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Reservas")


#Tabla Gestiona1
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Gestiona1'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Gestiona1',):
	sql_command="""
	CREATE TABLE Gestiona1(
		IdAdmin int REFERENCES Administrador(idAdmin),
		Dni int REFERENCES Trabajador(Dni),
		PRIMARY KEY(IdAdmin, Dni)
		);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Gestiona1")




#Tabla Realiza
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Realiza'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Realiza',):
	sql_command="""
	CREATE TABLE Realiza(
		Id_trabajador int REFERENCES Trabajador(id_trabajador),
	 	Id_reserva int REFERENCES Reserva(Id_reserva),
		PRIMARY KEY(Id_reserva)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Realiza")


#Tabla Gestiona2
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Gestiona2'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Gestiona2',):
	sql_command="""
	CREATE TABLE Gestiona2(
		Id_trabajador int REFERENCES Trabajador(DNI),
	 	Id_venta int REFERENCES Ventas(Identificador),
		PRIMARY KEY(Id_venta)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Gestiona2")



sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('54142189', 'Alberto Jesus', 'Lunes', '644136154', '10');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('94142188', 'Juan Brey', 'Miercoles', '344136154', '11');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('74142187', 'Luis Abascal', 'Jueves', '744136154', '16');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('64142186', 'Luque Infante', 'Lunes', '844136154', '17');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('44142185', 'Ana Jesus oso', 'Lunes', '944136154', '19');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('34142184', 'Carmen Jesu', 'Viernes', '144136154', '12');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('24142183', 'Sergio Lunaf', 'Martes', '634336154', '16');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('14142182', 'David Perezos', 'Lunes', '624126154', '18');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('74142181', 'Jorge Rub', 'Miercoles', '614136154', '11');"""
cursor.execute(sql_command)




sql_command="""INSERT INTO Gestiona2(Id_trabajador, Id_venta) VALUES
	('54142189', 'T4WTH5');"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Gestiona2(Id_trabajador, Id_venta) VALUES
	('54142189', '0OLTH5');"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Gestiona2(Id_trabajador, Id_venta) VALUES
	('51142189', 'ERTG5');"""
cursor.execute(sql_command)




sql_command="""INSERT INTO Ventas(Identificador, Matricula, DNI_cliente, Fecha_venta) VALUES
	('T4WTH5', 'DGFRGT', '54142189', 20181229);"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Ventas(Identificador, Matricula, DNI_cliente, Fecha_venta) VALUES
	('0OLTH5', '12FRGT', '45675189', 20181229);"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Ventas(Identificador, Matricula, DNI_cliente, Fecha_venta) VALUES
	('ERTG5', 'DGFFFT', '21142189', 20181229);"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Ventas(Identificador, Matricula, DNI_cliente, Fecha_venta) VALUES
	('T4WT5', 'DGFRGT', '7414217', 20181229);"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Ventas(Identificador, Matricula, DNI_cliente, Fecha_venta) VALUES
	('87TH5', 'FRRGT', '14142123', 20181229);"""
cursor.execute(sql_command)


print("Se han metido todos los datos en la BD")





#------------------------------------------------
# DISPARADOR // TRIGGER
#------------------------------------------------


sql_command="""CREATE TRIGGER IF NOT EXISTS validar_dni
	BEFORE INSERT ON Trabajador
	BEGIN
	SELECT
	CASE
	WHEN NEW.DNI / 10000000 < 1 OR NEW.DNI / 10000000 > 10 THEN
	RAISE (ABORT, 'DNI erróneo') END;
	END;"""
cursor.execute(sql_command)



#------------------------------------------------
# PROGRAMA PRINCIPAL
#------------------------------------------------

continuar= True

while continuar:
	print("\nMENU")
	print("1 - Dar de Alta un nuevo Trabajador")
	print("2 - Ver historial de ventas de un trabajador")
	print("3 - Ver historial de ventas de todos los trabajadores")
	print("4 - Salir")
	entrada= input("\nInserta un número del menú: ")
	if entrada == 1:
		dni = raw_input("\nDNI (sin letra): ")
		nombre= raw_input("Nombre y apellidos: ")
		horario= raw_input("Horario: ")
		telefono= raw_input("Teléfono : ")
		ventas=raw_input("Número de ventas realizadas :")

		cursor.execute("INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES (" + dni + ", " + `nombre` + ", " + `horario` + ", " + `telefono` + ", " + `ventas` + ");")
		print("")
		print(cursor.fetchall())

	elif entrada == 2:

		cual = raw_input("\nDNI del trabajador del que desea comprobar las ventas realizadas: ")
		cursor.execute("select * from Gestiona2 g inner join Ventas v on g.Id_Venta = v.Identificador where g.Id_trabajador= "+cual+";")

		print("")
		print(cursor.fetchall())

	elif entrada ==3:

		cursor.execute("select * from Gestiona2 g inner join Ventas v on g.Id_venta = v.Identificador")
		print("")
		print(cursor.fetchall())


	elif entrada == 4:
		continuar= False



#------------------------------------------------
# DESCONEXIÓN Y CIERRE
#------------------------------------------------

connection.commit()
connection.close()
