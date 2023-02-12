
import sys


def salto():

	print("")
	
	
	

def menu():

	print("Bienvenido al inventario de la ferretería: ")
	salto()
	print("¿Qué material quiere guardar?")
	salto()
	print("1. Tornillos")
	print("2. Tubos de fontanería")
	print("3. Destornilladores")
	print("4. Grifos")
	print("5. Material eléctrico")
	print("6. Salir del programa")
	salto()
	
	
	
	
def guardar():

	salto()
	try:
	
		nombre = input("Elija el nombre del material: ").upper()
		#Nos aseguramos que el nombre del material sea igual al de menú
		"""Usamos mayúsculas como forma de controlar que la palabra se introduzca correctamente. Se puede dar el caso
		de que introduzca la primera letra con minúscula, con mayúscula, una letra en medio en mayúscula... Al forzar que 
		el programa la convierta en mayúscula controlamos esos errores."""
		assert nombre == ("TORNILLOS") or nombre == ("TUBOS DE FONTANERÍA") or nombre == ("DESTORNILLADORES") or nombre == ("GRIFOS") or nombre == ("MATERIAL ELÉCTRICO")
		salto()
		cantidad = int(input("¿Cuantas unidades quiere guardar (Debe ser un número menor a 10000)?: "))
		#Nos aseguramos que sea una cantidad positiva y menor a 10000 unidades
		assert 0 < cantidad < 10000
		salto()
		precio = float(input("¿Cuál es el precio en euros de la unidad?: "))
		#Nos aseguramos que el precio no sea negativo
		assert precio > 0
		salto()
		descripcion = input("Incluya una descripción del material (Debe ser superior a 10 caracteres): ")
		#Nos aseguramos que la descripción sea suficiente
		assert len(descripcion) > 10
		salto()
		sys.exit("El material se ha guardado correctamente")
		
	
	except Exception as error:
		
		salto()
		print("El error cometido es del tipo: ", type(error).__name__)
		salto()
		sys.exit("Ha introducido algún tipo de dato no válido y no se puede guardar")
		
