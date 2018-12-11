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


#Tabla DarAlta
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarAlta'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarAlta',):
    sql_command="""
	CREATE TABLE DarAlta(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		fecha date,
		PRIMARY KEY(DNI, Identificador, fecha)
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


#Tabla DarAlta
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='DarBaja'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('DarBaja',):
    sql_command="""
	CREATE TABLE DarBaja(
		DNI varchar(9) REFERENCES Trabajador(DNI),
		Identificador int REFERENCES Administrador(Identificador),
		fecha date,
		PRIMARY KEY(DNI, Identificador, fecha)
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
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('44142185', 'Ana Jesus', 'Lunes', '944136154', '19');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('34142184', 'Carmen Jesus', 'Viernes', '144136154', '12');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('24142183', 'Sergio Luna', 'Martes', '634336154', '16');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('14142182', 'David Perez', 'Lunes', '624126154', '18');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('74142181', 'Jorge Rubian', 'Miercoles', '614136154', '1');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('64142139', 'Esteban Morales ', 'Lunes', '624136154', '22');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('84142129', 'Nuria Retrego', 'Lunes', '144136154', '42');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('57141189', 'Sergi Numan', 'Jueves', '644155154', '62');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('64145189', 'Alberto Parida', 'Lunes', '774136154', '32');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('64147180', 'Carmen Delgado', 'Martes', '684136154', '12');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('51149181', 'Luisma Mesus', 'Lunes', '694136154', '122');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('53144282', 'Sanamor Fuego', 'Jueves', '604136154', '112');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('54642573', 'Piedro juli', 'Martes', '600136154', '12');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('54542794', 'Berto Julian', 'Jueves', '614136154', '1');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('53142415', 'Simon Carmelo', 'Lunes', '624136154', '2');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('52142126', 'Julia Adie', 'Martes', '624136154', '3');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('94142237', 'Diego Jesus', 'Miercoles', '654136154', '6');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('84142448', 'Ismael Coleta', 'Martes', '656736154', '7');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('74142159', 'Rodri Perez', 'Lunes', '618536154', '1');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('64142169', 'Carlitos Fuerte', 'Miercoles', '123436154', '14');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('44142179', 'Santiago Grande', 'Lunes', '674136154', '11');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('34143119', 'Morado Azulado ', 'Martes', '876136154', '7');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('24144189', 'Barba luis', 'Jueves', '654136154', '9');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono, VentasRealizadas) VALUES ('14145189', 'Melchor Baltasar', 'Lunes', '984136154', '8');"""
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

    elif entrada ==3:
	sql_command="""SELECT * FROM Trabajador;"""
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
