
import sqlite3, sys
from consultas import *




def creacion():

	conexion = sqlite3.connect("datos.db")
	cursor = conexion.cursor()
	#Usamos IF NOT EXISTS para crear la tabla solo en caso de que no exista esta
	#El no hacerlo hará que tengamos un error al iniciar el programa más de una vez
	cursor.execute("CREATE TABLE IF NOT EXISTS Clientes (DNI TEXT PRIMARY KEY, Nombre TEXT, Telefono INTEGER, Direccion TEXT)")
	conexion.commit()
	conexion.close()
	
	



def salto():

	print("\n")
	
	
	

def menu():

	salto()
	print("####################################")
	print("BIENVENIDO A LA CONSULTA DE CLIENTES")
	print("####################################")
	salto()
	print("¿Qué operación desea realizar?:")
	salto()
	print("1. Guardar nuevo cliente")
	print("2. Consultar datos de un cliente")
	print("3. Borrar un cliente")
	print("4. Mostrar listado de clientes")
	print("5. Salir del programa")
	salto()
	
	
	
def trabajar(valor):
	
	
	if valor == 1:
	
		crear()
			
			
	
	elif valor == 2:
		
		leer()
		
	
	else:
	
		borrar()
		
	
	
	



if __name__ == '__main__':



    #Mandamos llamar a la función creación para crear la tabla
	creacion()
	
	while True:
	
		menu()
		opcion = int(input("Seleccione una opción numérica: "))
		
		
		if 1 <= opcion <= 3:
		
			trabajar(opcion)
		
			
			
		elif opcion == 4:
		
			mostrar()
			
			
		elif opcion > 5 or opcion < 1:
		
			salto()
			salto()
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print("DEBE ELEGIR UNA OPCIÓN ENTRE 1 Y 5")
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			salto()
			salto()
	
		else:
	
			salto()
			sys.exit("PROGRAMA TERMINADO")
		
		
		
		
		
	