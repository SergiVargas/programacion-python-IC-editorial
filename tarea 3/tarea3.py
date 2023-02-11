
#PROGRAMA PARA BUSCAR LOS DISTINTOS AMINOÁCIDOS EN LA CADENA


arn = "AUACAAAGAGAUGAUCAGGGUAUAAAGUCGAUACAAGACCAAGAUGGCUAUGCGAAACGUAGCGAUAUAUAAGAGACAGAAGCGUUAGCGCAAAUGAUAUGCAAAGGGUAUAGCCGUAGCUACGAGAAACGCAUAAUAAGGACCCUAUCGACAAUCGAUAGCCAAGAUGCUAAGCUACGAUUCGUA"

#Creamos el diccionario con los aminoácidos como clave
aminoacidos = {"metionina" : 0, "lisina" : 0, "glutamina" : 0}

#Recorremos la cadena buscando los patrones de los aminoácidos
for i in range(len(arn)):
     #Almacenamos el número de veces que aparecen 
     if arn[i : i+3] == "AUG":
             aminoacidos["metionina"] += 1
     if arn[i : i+3] == "AAA" or arn[i : i+3] == "AAG":
             aminoacidos["lisina"] += 1
     if arn[i : i+3] == "CAA" or arn[i : i+3] == "CAG":
             aminoacidos["glutamina"] += 1
			 
#Mostramos el resultado mediante una cadena a la que damos formato
print("En la secuencia están presentes los siguientes aminoácidos en la cantidad indicada: metionina -> {}, lisina -> {}, glutamina -> {}".format(aminoacidos["metionina"], aminoacidos["lisina"], aminoacidos["glutamina"]))
