# -*- coding: utf-8 -*-

#------------------------------------------------
# DATOS INICIALIZACIÓN
#------------------------------------------------

from datetime import date
import sqlite3
connection = sqlite3.connect("venta.db")

cursor= connection.cursor()

#cursor.execute("""DROP TABLE Trabajador;""")
#cursor.execute("""DROP TABLE Ventas;""")
#cursor.execute("""DROP TABLE Reservas;""")


#------------------------------------------------
# CREACIÓN DE TABLAS
#------------------------------------------------


# Tabla Trabajador

sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Trabajador';"""
cursor.execute(sql_command)
if cursor.fetchone() !=('Trabajador',):
    sql_command="""
	CREATE TABLE Trabajador(
		DNI int PRIMARY KEY,
		Nombre_apellidos varchar(50) NOT NULL,
		Horario varchar(100),
		Telefono int
	);"""

    cursor.execute(sql_command)
    print("Se ha creado la tabla Trabajador")


#Tabla Ventas
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Ventas'; """
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


#Tabla Reservas
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Reservas'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Reservas',):
    sql_command="""
	CREATE TABLE Reservas(
		Identificador int,
		Matricula varchar(10) REFERENCES Vehiculo(Matricula),
		DNI_cliente int,
		Fecha_realizada date,
		Fecha_entrega date,
		PRIMARY KEY(Identificador)
	);"""

    cursor.execute(sql_command)
    print("Se ha creado la tabla Reservas")


#Tabla Realiza
sql_command="""SELECT name FROM sqlite_master WHERE TYPE='table' AND name='Realiza'; """
cursor.execute(sql_command)
if cursor.fetchone() !=('Realiza',):
    sql_command="""
	CREATE TABLE Realiza(
		Identificador int REFERENCES Reservas(Identificador),
		DNI_trabajador int REFERENCES Trabajador(DNI),
		PRIMARY KEY(Identificador)
	);"""

    cursor.execute(sql_command)
    print("Se ha creado la tabla Realiza")


sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono) VALUES ('54142189', 'Alberto Jesus', 'Lunes', '644136154');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono) VALUES ('94142188', 'Juan Brey', 'Miercoles', '344136154');"""
cursor.execute(sql_command)
sql_command="""INSERT INTO Trabajador(DNI, Nombre_apellidos, Horario, Telefono) VALUES ('74142187', 'Luis Abascal', 'Jueves', '744136154');"""
cursor.execute(sql_command)

cursor.execute("INSERT INTO Reservas(Identificador, Matricula, DNI_cliente, Fecha_realizada, Fecha_entrega) VALUES ('1', '1234ASD', '12345678', '01-02-2019', '03-04-2019');")
cursor.execute("INSERT INTO Realiza(Identificador, DNI_Trabajador) VALUES ('1', '54142189');")

cursor.execute("INSERT INTO Reservas(Identificador, Matricula, DNI_cliente, Fecha_realizada, Fecha_entrega) VALUES ('2', '5678ASD', '87654321', '01-02-2019', '03-04-2019');")
cursor.execute("INSERT INTO Realiza(Identificador, DNI_Trabajador) VALUES ('2', '54142189');")

cursor.execute("INSERT INTO Reservas(Identificador, Matricula, DNI_cliente, Fecha_realizada, Fecha_entrega) VALUES ('3', '4444DDD', '75577655', '01-02-2019', '03-04-2019');")
cursor.execute("INSERT INTO Realiza(Identificador, DNI_Trabajador) VALUES ('3', '94142188');")

print("Se han metido todos los datos en la BD")





#------------------------------------------------
# DISPARADOR // TRIGGER
#------------------------------------------------


sql_command="""CREATE TRIGGER IF NOT EXISTS validar_fecha
	BEFORE INSERT ON Reservas
	BEGIN
	SELECT
	CASE
	WHEN NEW.Fecha_realizada > NEW.Fecha_entrega THEN
	RAISE (ABORT, 'No puede ser entregado un coche antes de realizar la reserva') END;
	END;"""
cursor.execute(sql_command)



#------------------------------------------------
# PROGRAMA PRINCIPAL
#------------------------------------------------

continuar= True

while continuar:
    print("\nMENU")
    print("1 - Realizar una reserva")
    print("2 - Ver historial de reservas de un trabajador")
    print("3 - Ver historial de reservas de todos los trabajadores")
    print("4 - Salir")
    entrada= input("\nInserta un número del menú: ")
    if entrada == 1:
        identificador = raw_input("\nIdentificador de la venta: ")
        matricula= raw_input("Matricula del coche: ")
        clienteDNI= raw_input("DNI del cliente: ")
	vendedor= raw_input("DNI del vendedor: ")
        fechaRealizado= raw_input("Fecha del día de la venta :")
	fechaEntrega= raw_input("Fecha del día de la entrega :")

        cursor.execute("INSERT INTO Reservas(Identificador, Matricula, DNI_cliente, Fecha_realizada, Fecha_entrega) VALUES (" + identificador + ", " + `matricula` + ", " + `clienteDNI` + ", " + `fechaRealizado` + ", " + `fechaEntrega` + ");")
	cursor.execute("INSERT INTO Realiza(Identificador, DNI_Trabajador) VALUES (" + identificador + ", " + `vendedor` + ");")
	print("")
        print(cursor.fetchall())

    elif entrada == 2:
	cual = raw_input("\nDNI del trabajador del que desea comprobar las reservas realizadas: ")
        cursor.execute("select * from Realiza r INNER JOIN Reservas re on r.Identificador = re.Identificador where DNI_Trabajador= "+cual+";")

        print("")
        print(cursor.fetchall())

    elif entrada ==3:
	sql_command="""select * from Realiza r INNER JOIN Reservas re on r.Identificador = re.Identificador;"""
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
