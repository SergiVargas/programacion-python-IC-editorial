
				
				
from utilidades import *



if __name__ == '__main__':
    
	
#Esta librería permite manejar opciones para interactuar con el intérprete
	import sys
	
	
	while True:
		
		
		menu()
		opcion = int(input('Ingrese una opción del menú para seguir: '))
		#Forzamos que la opción sea un número válido
		assert opcion > 0 and opcion < 7, "Debe elegir una opción entre 1 y 6"
		if 0 < opcion <=5 :
			guardar()
			
		else:
		
			salto()
			#Este comando cierra la aplicación
			sys.exit("Se cierra el programa, adios")
		
		
	