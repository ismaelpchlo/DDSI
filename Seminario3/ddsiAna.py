# -*- coding: utf-8 -*-

#------------------------------------------------
# DATOS INICIALIZACIÓN
#------------------------------------------------

from datetime import date
import sqlite3
connection = sqlite3.connect("vehiculos.db")

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


# Tabla Vehículo

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Vehiculo';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Vehiculo',):
	sql_command="""
	CREATE TABLE Vehiculo(
		Matricula varchar(10) PRIMARY KEY,
		Marca varchar(15) NOT NULL,
		Modelo varchar(20),
		Disponibilidad varchar2(15) CHECK (Disponibilidad IN ('stock', 'agotado', 'reservado', 'encargado')),
		Precio int
	);"""

	cursor.execute(sql_command)
	print("Se ha creado la tabla Vehiculo")

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


sql_command="""INSERT INTO Encargar(Identificador, IdentificadorP, Matricula, Fecha) VALUES
	('1234', '000', '4289XVT', '10-12-2018');"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Encargar(Identificador, IdentificadorP, Matricula, Fecha) VALUES
	('1234', '001', '9932KLC', '01-11-2018');"""
cursor.execute(sql_command)

sql_command="""INSERT INTO Encargar(Identificador, IdentificadorP, Matricula, Fecha) VALUES
	('1234', '010', '0529DPN', '17-01-2019');"""
cursor.execute(sql_command)


sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('000', 'Mercedes');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('001', 'Audi');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('010', 'Peugeot');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('011', 'Suzuki');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('100', 'Renault');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('101', 'BMW');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('110', 'Toyota');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Proveedor(IdentificadorP, Nombre_empresa) VALUES ('111', 'Seat');"""
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
	'\nPrecio de vehículo no válido'
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
		proveedor = raw_input("\nCódigo del proveedor: ")
		matricula = raw_input("\nMatrícula del vehículo: ")

		cursor.execute("INSERT INTO Encargar(Identificador, IdentificadorP, Matricula, Fecha) VALUES	(" + admin + ", " + proveedor + ", " + `matricula` + ", '22-01-2019');")
		
		cursor.execute("select * from Encargar e inner join Vehiculo v on e.Matricula = v.Matricula where e.IdentificadorP= "+proveedor+";")

		print("")
		print(cursor.fetchall())

	elif entrada ==3:

		cursor.execute("select * from Encargar e inner join Vehiculo v on e.Matricula = v.Matricula")
		print("")
		print(cursor.fetchall())

	elif entrada == 4:
		continuar= False



#------------------------------------------------
# DESCONEXIÓN Y CIERRE
#------------------------------------------------

connection.commit()
connection.close()
