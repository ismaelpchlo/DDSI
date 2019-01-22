# -*- coding: utf-8 -*-

#------------------------------------------------
# DATOS INICIALIZACIÓN
#------------------------------------------------

from datetime import date
import sqlite3
connection = sqlite3.connect("vehiculos.db")

cursor= connection.cursor()

#cursor.execute("""DROP TABLE Administrador;""")
#cursor.execute("""DROP TABLE Vehiculo;""")
#cursor.execute("""DROP TABLE Proveedor;""")
#cursor.execute("""DROP TABLE Trabajador;""")
#cursor.execute("""DROP TABLE Encargar;""")
#cursor.execute("""DROP TABLE Anular;""")
#cursor.execute("""DROP TABLE DarAlta;""")
#cursor.execute("""DROP TABLE DarBaja;""")
#cursor.execute("""DROP TABLE Consultar;""")
#cursor.execute("""DROP TABLE Disponible;""")

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


# Tabla Vehículo

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Vehiculo';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Vehiculo',):
	sql_command="""
	CREATE TABLE Vehiculo(
	   Matricula varchar(100) PRIMARY KEY NOT NULL,
      Marca varchar(15) NOT NULL,
	   Modelo varchar(20),
	   Disponibilidad varchar2(15) 
         CHECK (Disponibilidad IN ('stock', 'agotado','reservado', 'encargado')),
	   Precio int
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Vehículo")

#Tabla Proveedor

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


#Tabla Encargar

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Encargar'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Encargar',):
	sql_command="""
	CREATE TABLE Encargar(
		Identificador int REFERENCES Administrador(Identificador),
	  IdentificadorP int REFERENCES Proveedor(IdentificadorP),
	  Modelo varchar(20) REFERENCES Vehiculo(Modelo),
	  PRIMARY KEY(Identificador, IdentificadorP, Modelo)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Encargar")


#Tabla Anular

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Anular'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Anular',):
	sql_command="""
	CREATE TABLE Anular(
		Identificador int REFERENCES Administrador(Identificador),
	  IdentificadorP int REFERENCES Proveedor(IdentificadorP),
	  PRIMARY KEY(Identificador, IdentificadorP)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Anular")


#Tabla DarAlta

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarAlta'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarAlta',):
	sql_command="""
	CREATE TABLE DarAlta(
		Identificador int REFERENCES Administrador(Identificador),
	   Matricula varchar(10) REFERENCES Vehiculo(Matricula),
	   Marca varchar(15) NOT NULL,
	   Modelo varchar(20),
	   Disponibilidad CHECK (Disponibilidad IN ('stock', 'agotado', 'reservado', 'encargado')),
	   Precio int,
	   PRIMARY KEY(Identificador, Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla DarAlta")

#Tabla DarBaja

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarBaja'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarBaja',):
	sql_command="""
	CREATE TABLE DarBaja(
		Identificador int REFERENCES Administrador(Identificador),
	   Matricula varchar(10) REFERENCES Vehiculo(Matricula),
	   PRIMARY KEY(Identificador, Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla DarBaja")


#Tabla Consultar

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Consultar'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Consultar',):
	sql_command="""
	CREATE TABLE Consultar(
	   Disponibilidad CHECK (Disponibilidad IN ('stock')),
	   Matricula varchar(10) PRIMARY KEY REFERENCES Vehiculo(Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Consultar")


#Tabla Disponible

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Disponible'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Disponible',):
	sql_command="""
	CREATE TABLE Disponible(
	   Matricula varchar(10) PRIMARY KEY REFERENCES Vehiculo(Matricula)
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Disponible")




sql_command="""INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES ('6745GTT', 'Daewoo', 'Lanos', 'stock', '12000');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES ('5893HHM', 'Renault', 'Laguna', 'reservado', '18000');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES ('9932KLC', 'Audi', 'A5', 'encargado', '29000');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES ('0529DPN', 'Peugeot', '5008', 'agotado', '25000');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES ('4289XVT', 'Mercedes', 'CLASE SL', 'encargado', '130000');"""
cursor.execute(sql_command)





#------------------------------------------------
# DISPARADOR // TRIGGER
#------------------------------------------------


sql_command="""CREATE TRIGGER IF NOT EXISTS  validar_precio
	BEFORE INSERT ON Vehiculo
	BEGIN
	SELECT
	CASE
	WHEN NEW.Precio < 0 THEN
	RAISE (
	ABORT,
	'Precio de vehículo no válido'
	)
	END;
	END;"""
cursor.execute(sql_command)



#------------------------------------------------
# PROGRAMA PRINCIPAL
#------------------------------------------------

continuar= True

while continuar:
	print("\nMENU")
	print("1 - Dar de alta un nuevo vehículo")
	print("2 - Encargar vehículo a proveedor")
	print("3 - Mostrar encargos")
	print("4 - Salir")
	entrada= input("\nInserta un número del menú: ")
	if entrada == 1:
		matricula = raw_input("\nMatrícula: ")
		marca= raw_input("Marca: ")
		modelo= raw_input("Modelo: ")
		disponibilidad= raw_input("Disponibilidad: ")
		precio=raw_input("Precio: ")

		cursor.execute("INSERT INTO Vehiculo(Matricula, Marca, Modelo, Disponibilidad, Precio) VALUES (" + `matricula` + ", " + `marca` + ", " + `modelo` + ", " + `disponibilidad` + ", " + `precio` + ");")
		print("")
		print(cursor.fetchall())

	elif entrada == 2:
		admin = raw_input("\nIntroduzca su identificador de Administrador: ")
		proveedor = raw_input("\nMarca del vehículo a encargar: ")
		modelo = raw_input("\nModelo del vehículo a encargar: ")

		cursor.execute("INSERT INTO Encargar(Identificador, IdentificadorP, Modelo) VALUES (" + admin + ", " + `proveedor` + ", " + `modelo` + ");")
		print("")
		print(cursor.fetchall())

	elif entrada ==3:
		sql_command="""SELECT * FROM Encargar;"""
		cursor.execute(sql_command)
		print("")
		print(cursor.fetchall())

	elif entrada == 4:
		continuar= False



#------------------------------------------------
# DESCONEXIÓN Y CIERRE
#------------------------------------------------

connection.commit()
connection.close()
