
#PROGRAMA PARA BUSCAR TRIPTÓFANO DENTRO DE UNA CADENA DE ARN

#Tenemos la cadena en bruto de ARN
arn = "AOUCUGGUGGGGAUCUGTTGAAAAUUGGUGCUGGCOGGGUGGCUUGGATUAUGGUACGGOCUAUAGCCAAGCUGTTUAGCUAUGGUGCGGGUUUCAOGUUCUGGAGCUAUGCGCAUTOTOUUAGCUGGGAUAGCGGCAUAUGGUCGGGTGTCAGGAGOOAGAGCUAGCGAUUGGCGGCGAUAGCGCAUAGCAUU"

#Limpiamos la cadena del carácter extraño T
#Para eso usamos la función .split()
subc1 = arn.split("T")

#La función .split() produce una lista de cadenas
#Volvemos a unir la cadena ya limpia del primer carácter extraño
"""Elegimos la doble comilla "", que no deja ningún espacio,
 para que no haya ningún carácter añadido a la nueva cadena"""
arn = "".join(subc1)

#Limpiamos la cadena del carácter extraño O
subc2 = arn.split("O")

#Volvemos a unir la cadena
arn = "".join(subc2)

#Buscamos el número de tripletas que codifican el triptofano
triptofano = arn.count("UGG")

#Mostramos el resultado por pantalla
print("El número de tripletas de nucleótidos que codifican el triptófano en esta cadena de ARN es: " + str(triptofano))
