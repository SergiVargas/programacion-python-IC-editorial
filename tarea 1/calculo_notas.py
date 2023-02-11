
#PROGRAMA PARA CALCULAR LA NOTA MEDIA Y LA CALIFICACIÓN FINAL
nombre = input ("Introduce el nombre del alumno: ")
historia = float(input("Introduce la nota de historia: "))
mates = float(input("Introduce la nota de matemáticas: "))
fisica = float(input("Introduce la nota de física: "))
biologia = float(input("Introduce la nota de biología: "))
lengua = float(input("Introduce la nota de lengua: "))

nota = (historia + mates + fisica + biologia + lengua) / 5

print("La nota media final del alumno " + nombre + " es " + str(nota))

if (nota >= 5 and nota < 6):
	print ("Calificación final SUFICIENTE")
	
elif (nota >= 6 and nota < 7):
	print ("Calificación final BIEN")
	
elif (nota >= 7 and nota < 9):
	print ("Calificación final NOTABLE")
	
elif (nota >= 9 and nota < 10):
	print ("Calificación final SOBRESALIENTE")
	
elif (nota == 10):
	print ("Calificación final MATRÍCULA")
	
else:
	print("Calificación final SUSPENSO")
