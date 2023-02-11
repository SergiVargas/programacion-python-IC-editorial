

def menu():


	"""
	Esta función muestra el menú de entrada
	a la aplicación. Permite introducir los
	datos necesarios.
			
			
	Args:
			
		Ninguno
				
	Returns:

		Los datos para poder realizar los cálculos
		y llama a la siguiente función para que 
		continue el flujo del programa		
			  
	"""

		
		
	salto()
	linea_divisoria()
	salto()
	print("CÁLCULO DE IMPORTES DE IVA")
	salto()
	linea_divisoria()
	"""Ponemos esta variable global para hacerla accesible
	desde diversas partes del programa"""
	global importe 
	salto()
	importe = float(input("INTRODUZCA EL IMPORTE: "))
	salto()
	print ("SELECCIONE EL TIPO DE IVA (MEDIANTE UN NÚMERO):")
	print("1.GENERAL")
	print("2.REDUCIDO")
	print("3.SUPERREDUCIDO")
	salto()
	tipo = input()
	salto()
	tipo_IVA(tipo)
				
				


def calculo(impuesto):

	IVA = importe * impuesto
	total = importe + IVA
	resultado(IVA, total)
	
	
	


def tipo_IVA(tipo):

    
	if tipo == "1":
		calculo(0.21)
		
	
	elif tipo == "2":
		calculo(0.10)
	
	elif tipo == "3":
		calculo(0.04)
		
	else:
		salto()
		print ("Tipo de IVA incorrecto")
		





def resultado(IVA, total):
    
	"""
	Esta función muestra por pantalla el desglose
	de la factura con el resultado de las operaciones
		
	Args:
		
		IVA (float): valor del IVA de la compra
		total (float): importe total de la compra

    Returns:

		Un menú de pantalla con el desglose final		
		  
	"""
	
	
	linea_divisoria()
	salto()
	print("ESTE ES EL DESGLOSE DE LA FACTURA: ")
	salto()
	#La función round() nos permite redondear un número decimal
	print("EL IMPORTE DE LA COMPRA ES DE {} EUROS".format(round(importe, 2)))
	salto()
	print("EL IVA PARA ESTA COMPRA ES DE {} EUROS".format(round(IVA, 2)))
	salto()
	print("LA CANTIDAD TOTAL A COBRAR ES DE {} EUROS".format(round(total, 2)))
	salto()
	linea_divisoria()

	



def linea_divisoria():
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

	
	

def salto():
	print("")







#Punto de entrada
if __name__ == '__main__':

	menu()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	