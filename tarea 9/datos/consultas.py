import sqlite3
from menu import salto



def crear():


    #Introducimos por teclado los datos del cliente a crear
	DNI = input("Introduzca el DNI sin letra: ")
	nombre = input ("Introduzca el nombre: ")
	telefono = input("Introduzca el teléfono: ")
	direccion = input("Introduzca la dirección: ")
	
	#Los guardamos en un arreglo para facilitar su inserción en la base de datos
	misdatos = [DNI, nombre, telefono, direccion]
	
	
	conexion = sqlite3.connect("datos.db")
	cursor = conexion.cursor()
	#Utilizamos "?" para indicar que son parámetros a introducir en la consulta y no un dato predefinido
	cursor.execute("INSERT INTO Clientes VALUES(?,?,?,?)", misdatos)
	conexion.commit()
	conexion.close()
	salto()
	print("CLIENTE CREADO")
	salto()
	
	
	
	
	
def leer():
	
	conexion = sqlite3.connect("datos.db")
	cursor = conexion.cursor()
	#Buscamos el cliente por el DNI, al ser una clave única
	salto()
	DNI = input("Introduzca el DNI sin letra del cliente a consultar: ")
	salto()
	cursor.execute("SELECT * FROM Clientes WHERE DNI = " + DNI)
	cliente = cursor.fetchone()
	print("LOS DATOS DEL CLIENTE INTRODUCIDO SON: ")
	salto()
	print(cliente)
	salto()
	conexion.commit()
	conexion.close()
	
	
	
	
	
def borrar():
	
	
	conexion = sqlite3.connect("datos.db")
	cursor = conexion.cursor()
	#Buscamos también por el DNI del cliente
	salto()
	DNI = input("Introduzca el DNI sin letra del cliente que desea borrar: ")
	cursor.execute("DELETE FROM Clientes WHERE DNI = " + DNI)
	conexion.commit()
	salto()
	print("CLIENTE BORRADO")
	salto()
	conexion.close()
	
	


def mostrar():

	conexion = sqlite3.connect("datos.db")
	cursor = conexion.cursor()
	cursor.execute("SELECT * FROM Clientes")
	clientes = cursor.fetchall()
	salto()
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("ESTA ES LA LISTA DE CLIENTES:")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	salto()
	#Recorremos con un bucle for para mostrar de uno en uno
	for cliente in clientes:
		print(cliente)
	conexion.close()
	salto()
	salto()
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	salto()
	salto()
	
		
	