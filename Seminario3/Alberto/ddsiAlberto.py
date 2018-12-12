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
#cursor.execute("""DROP TABLE Ventas;""")
#cursor.execute("""DROP TABLE Historial;""")
#cursor.execute("""DROP TABLE DarAlta;""")
#cursor.execute("""DROP TABLE DarBaja;""")
#cursor.execute("""DROP TABLE Consulta;""")
#cursor.execute("""DROP TABLE ModificaDatos;""")

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


# Tabla Ventas
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Ventas';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Ventas',):
	sql_command="""
	CREATE TABLE Ventas(
		Matricula varchar(10),
		Nombre_cliente varchar(50) NOT NULL,
		DNI_cliente int,
		DNI_vendedor int REFERENCES Trabajador(DNI),
		Importe int,
		Fecha_venta date,
		Fecha_Entrega date,
		PRIMARY KEY(DNI_cliente, DNI_vendedor, Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Ventas")





#Tabla DarAlta
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarAlta'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarAlta',):
	sql_command="""
	CREATE TABLE DarAlta(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		PRIMARY KEY(DNI, Identificador)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla DarAlta")


#Tabla Historial
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Historial'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Historial',):
	sql_command="""
	CREATE TABLE Historial(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		fecha date,
		PRIMARY KEY(DNI, Identificador, fecha)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Historial")


#Tabla DarBaja
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarBaja'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarBaja',):
	sql_command="""
	CREATE TABLE DarBaja(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		PRIMARY KEY(DNI, Identificador)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla DarBaja")


#Tabla Consulta
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Consulta'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Consulta',):
	sql_command="""
	CREATE TABLE Consulta(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		fecha date,
		PRIMARY KEY(DNI, Identificador, fecha)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Consulta")


#Tabla ModificaDatos
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='ModificaDatos'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('ModificaDatos',):
	sql_command="""
	CREATE TABLE ModificaDatos(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		fecha date,
		PRIMARY KEY(DNI, Identificador, fecha)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla ModificaDatos")




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



sql_command="""INSERT INTO Ventas(Matricula, Nombre_cliente, DNI_cliente, DNI_vendedor, Importe, Fecha_venta, Fecha_Entrega ) VALUES
	('T4WTH5', 'Laura Neko', '12234553', '54142189', '22.000', 20181219, 20181229);"""

sql_command="""INSERT INTO Ventas(Matricula, Nombre_cliente, DNI_cliente, DNI_vendedor, Importe, Fecha_venta, Fecha_Entrega ) VALUES
	('LKIU15', 'Elena Olmo', '43284983', '54142189', '20.000', 20181217, 20181219);"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Ventas(Matricula, Nombre_cliente, DNI_cliente, DNI_vendedor, Importe, Fecha_venta, Fecha_Entrega ) VALUES
	('DDSIK1', 'Rosi Liante', '87352417', '54142189', '17.000', 20181117, 20181201);"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Ventas(Matricula, Nombre_cliente, DNI_cliente, DNI_vendedor, Importe, Fecha_venta, Fecha_Entrega ) VALUES
	('HF74F5', 'Ana Pena', '25384918', '54142189', '172.000', 20180617, 20180801);"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Ventas(Matricula, Nombre_cliente, DNI_cliente, DNI_vendedor, Importe, Fecha_venta, Fecha_Entrega ) VALUES
	('CFRTWW', 'Sam Mikrush', '75648392', '54142189', '12.000', 20180618, 20180802);"""
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
		cursor.execute("select * from Trabajador where DNI= "+cual+";")

		print("")
		print(cursor.fetchall())

		cursor.execute("select *  from Ventas where DNI_vendedor= "+cual+";")
		print("")
		print(cursor.fetchall())


	elif entrada ==3:

		sql_command1="""select * FROM Trabajador;"""
		cursor.execute(sql_command1)
		print("")
		print(cursor.fetchall())

		print("Historial de ventas de los trabajadores ")
		sql_command2="""select * FROM Ventas;"""
		cursor.execute(sql_command2)
		print("")
		print(cursor.fetchall())


	elif entrada == 4:
		continuar= False



#------------------------------------------------
# DESCONEXIÓN Y CIERRE
#------------------------------------------------

connection.commit()
connection.close()
