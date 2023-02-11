
#Importamos las clases para poder usarlas
from jugadores import Tenista, Ajedrecista, Futbolista




def espacio():
	
	print ("")
	

	
def separacion():
	
	print("#################################################")
	
	

#Menú principal de la aplicación	
def menu():

	espacio()
	separacion()
	espacio()
	print("BIENVENIDO A LA APLICACIÓN PARA CREAR DEPORTISTAS")
	espacio()
	separacion()
	espacio()
	espacio()
	print("¿Qué tipo de deportista quieres crear?")
	espacio()
	print("1. Tenista")
	print("2. Ajedrecista")
	print("3. Futbolista")
	print("4. Salir del menú")
	espacio()
	global valor
	valor = int(input("Selecciona un número del menú: "))
	espacio()
	
	
#Partes que comparten los tres tipos de deportistas	
def caracteristicas_comunes():
	
	global nombre, edad, altura
	espacio()
	separacion()
	espacio()
	print("Introduce los datos del deportista: ")
	nombre = input("¿Cuál es el nombre?: ")
	edad = int(input("¿Cuántos años tiene?: "))
	altura = int(input ("¿Cuál es su altura en cm?: "))
	
	

#Creamos los menús para los tres tipos de deportistas
def menu_tenista():
	
	caracteristicas_comunes()
	velocidad = int(input("¿Cuál es la velocidad de 0 a 50?: "))
	saque = int(input("¿Cuál es la potencia de saque de 0 a 30?: "))
	ganados = int(input("¿Cuantos partidos ha ganado a lo largo de su carrera?: "))
	grandes = int(input("¿Cuántos grand slams ha ganado?: "))
	tenista = Tenista(nombre, edad, altura, velocidad, saque, ganados, grandes)
	espacio()
	tenista.creacion()
	espacio()
	tenista.mostrar_datos()
	
	
	
	


def menu_ajedrecista():
	
	caracteristicas_comunes()
	maestro = input("¿Es Gran Maestro?(sí/no): ")
	ganadas = int(input("¿Cuántas partidas ha ganado a lo largo de su carrera?: "))
	tablas = int(input("¿Cuántas partidas han terminado en tablas a lo largo de su carrera?: "))
	puntos = int(input("¿Cuántos punto ELO tiene?: "))
	ajedrecista = Ajedrecista(nombre, edad, altura, maestro, ganadas, tablas, puntos)
	espacio()
	ajedrecista.creacion()
	espacio()
	ajedrecista.mostrar_datos()
	
	



def menu_futbolista():
	
	caracteristicas_comunes()
	velocidad = int(input("¿Cuál es la velocidad de 0 a 50?: "))
	seleccion = input("¿Ha jugado con su selección (sí/no): ")
	disparo = int(input("¿Cuál es su potencia de disparo de 0 a 30?: "))
	titulos = int(input("¿Cuántos títulos ha ganado?: "))
	futbolista = Futbolista(nombre, edad, altura, velocidad, seleccion, disparo, titulos)
	espacio()
	futbolista.creacion()
	espacio()
	futbolista.mostrar_datos()
	




#Iniciamos la aplicación
if __name__ == "__main__":

	
	menu()
	if valor > 0 and valor < 5 :
		
	   
		if valor == 1:
		
			menu_tenista()
		
			
		elif valor == 2:
		
			menu_ajedrecista()
				
			
		elif valor == 3:
		
			menu_futbolista()
			
				
		elif valor == 4:
		
			print("Hasta la próxima")
				
			
		
	else:
		print("Opción incorrecta")
		
		
		

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	