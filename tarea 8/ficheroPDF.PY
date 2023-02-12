
"""
Hay diferentes maneras de trabajar con los archivos PDF en Python.
Una de las más usadas es instalar el módulo PyPDF2. Con el podemos 
realizar diferentes funciones en los archivos PDF, tales como unirlos, extraer el contenido, rotarlos...

"""



#Importamos la librería previamente instalada
import PyPDF2

#Pedimos el nombre del fichero a convertir
nombre_fichero = input("¿Cómo se llama el fichero a convertir?: ")

#Pedimos el nombre del fichero txt resultante
nombre_convertido = input("¿Cómo se llamará el fichero tras la conversión?: ")

#Abrimos el PDF en modo leer binario
objetoPDF = open(nombre_fichero, "rb")

#Creamos un objeto del tipo PdfFileReader
#Aquí se lee el contenido del fichero abierto
leerPDF = PyPDF2.PdfFileReader(objetoPDF)

#Con este método guardamos el número de páginas del archivo
numero_paginas = leerPDF.numPages

#Mostramos un mensaje con el número de páginas
print("El fichero a convertir tiene " + str(numero_paginas) + " páginas")



#Recorremos las páginas con un bucle for
for pagina in range(numero_paginas):	

#Creamos el archivo txt e incorporamos la extensión al nombre
#Usamos el modo "a" para escribir tras la última información
	with open(nombre_convertido + ".txt", "a") as fichero:
        
#El método getPage() guarda el contenido de esta
		contenidoPagina = leerPDF.getPage(pagina)
		
#El método extracText() extrae el contenido como una cadena de texto		
		texto = contenidoPagina.extractText()
		
#Escribimos en el fichero de texto el contenido		
		fichero.writelines(texto)
	


"""

Tras estos pasos, si quisiéramos mostrar el contenido del fichero txt por pantalla, sólo tendríamos que abrirlo en modo lectura e imprimir su contenido.

"""


