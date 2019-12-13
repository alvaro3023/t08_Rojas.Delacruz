print("EJERCICIO N°1")
#              1         2         3         4
#    01234567890123456789012345678901234567890123456
cad="CAMARON QUE SE DUERME, SE LO LLEVA LA CORRIENTE"

#Reconocer el lugar de las siguientes letras:
#A
#C
#D
#E
#L
#M
#N

print(cad[1]) # Se reconocio la 1era A
print(cad[0]) # Se reconocio la 1era C
print(cad[15]) # Se reconocio la letra D
print(cad[10]) # Se reconocio la 1era E
print(cad[26]) # Se reconocio la L
print(cad[19]) # Se reconocio la 2da M
print(cad[44]) # Se reconocio la 2da N




print("EJERCICIO N°2")
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
cad="LOS AMORES QUE SE MARCHAN YA NO VUELVEN, DEJAN PENAS Y DOLOR"

# Contabilizar cuantas vocales O hay en la cadena
print(cad.count("O"))

# contabilizar cuantas vocales A hay en la cadena
print(cad.count("A"))

# Dar a conocer la letra de posicion -19
print(cad[-19]) # La letra es la D

# Dar a conocer la letra de  posicion 38
print(cad[38]) # La letra es la N

# Contabilizar cuantas vocales E hay en la cadena
print(cad.count("E"))


print("EJERCICIO N°3")
#              1         2
#    01234567890123456789012345678
cad="PIENSA EN GLOBAL, ACTUA LOCAL "

# De la siguiente cadena obtener las siguientes letras y vocales:
# N
# L la 1era
# O la 2da
# A la 4ta
# G

print(cad[3]) # Se reconocio la letra N
print(cad[15]) # Se reconocio la 1era L
print(cad[25]) # Se reconocio la 2da O
print(cad[27]) # Se reconocio la 4ta A
print(cad[10]) # Se reconocio la letra G




print("EJERCICIO N°4")
#              1         2         3
#    012345678901234567890123456789012
cad="WHERE THERE IS LOVE THERE IS LIFE"

# De la cadena obtener lo siguiente:
# cantidad de la vocal E
# La 5ta E
# La 2da T
# La 3era R
# La letra F

print(cad.count("E"))
print(cad[22])
print(cad[20])
print(cad[23])
print(cad[31])


print("EJERCICIO N°5")
#              1         2         3         4         5         6         7         8         9
#    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
cad="UNA MAÑANA ME LEVANTE Y MATE A UN ELEFANTE EN PIJAMA. ME PREGUNTO: ¿COMO SE PUSO LA PIJAMA?"


# De la cadena obtener lo siguiente:
# Cantidad de O
# Cantidad de I
# La letra de la ubicacion -34
# La letra de la ubicacion -43
# Obtener la cadena ANTON
print(cad.count("O")) # Se obtuvieron 6 "O"
print(cad.count("I")) # Se obtuvieron 6 "I"
print(cad[-35]) # Se descubrio la letra A
print(cad[-42]) # Se descubrio la letra D
print(cad[3] + cad[19] + cad[32] + cad[38] + cad[42]) # Se obtuvo el nombre ANTON


print("EJERCICIO N°6")
#              1         2         3
#    012345678901234567890123456789012345678
cad="DON'T DREAM YOUR LIFE, LIVE YOUR DREAMS"

# De la cadena descubrir que letra es la que ocupa las posiciones:
# 28
# 38
# -24
# -7
# Identificar cuantas veces se repite la cadena "DREAM"
print(cad[28]) # Se descubrio la letra Y
print(cad[38]) # Se descubrio la letra S
print(cad[-25]) # Se descubrio la letra U
print(cad[-8]) # Se descubrio la letra R
print(cad.count("DREAM"))


print("EJERCICIO N°7")
#              1         2         3         4
#    01234567890123456789012345678901234567890123456
cad="RICARDO PALMA SORIANO, EL BIBLIOTECARIO MENDIGO"

# De la cadena obtener lo siguiente:
# Cantidad de O
# Cantidad de I
# La letra de la ubicacion -34
# La letra de la ubicacion -43
# Obtener la cadena ANTON
print(cad.count("O")) # Se obtuvieron 6 "O"
print(cad.count("I")) # Se obtuvieron 6 "I"
print(cad[-35]) # Se descubrio la letra A
print(cad[-42]) # Se descubrio la letra D
print(cad[3] + cad[19] + cad[32] + cad[38] + cad[42]) # Se obtuvo el nombre ANTON


print("EJERCICIO N°8")
#              1         2         3         4
#    0123456789012345678901234567890123456789012
cad="YO NO SE, QUE ES LO QUE PASA CUANDO TE MIRO"

# De la cadena obtener lo siguiente
# Cuantas N se contabilizan
# La vocal de la posicion 38
# La letra de la posicion -26
# Cuantas veces se repite la cadena QUE
print(cad.count("N"))
print(cad[38]) # La letra reconocida es la E
print(cad[-26]) # La letra reconocida es la L
print(cad.count("QUE")) # Se reconoce que la cadena QUE se repite dos veces


print("EJERCICIO N°9")
#              1         2         3         4         5         6         7         8
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
cad="!EL INGENIO ESTA EN LA MENTE DE TODOS, DEPENDE DE UNO MISMO UTILIZARLA DE LA MEJOR MANERA!"

# De la cadena obtener lo sigueinte:
# Formar la cadena PENDIENTE
# Obtener la 4ta A
# Obtener la 8ava E
# Cantidad de N

print(cad[41] + cad[12] + cad[43] + cad[34] + cad[4] + cad[78] + cad[8] + cad[32] + cad[86])



print("EJERCICIO N°10")
#              1         2         3         4         5         6
#    01234567890123456789012345678901234567890123456789012345678901234
cad="SI PARA VIVIR NECESITO DE TUS BESOS, ENTONCES ME CONSIDERO MUERTO"

# De la cadena obtener lo sigueinte:
# Contar cuantas I existen en la cadena
# Contar cuantas O existen el la siguiente cadena
# La letra ubicada en la posicion 45 es:
# La 4ta O

print(cad.count("I")) # Se contaron 5 I
print(cad.count("O")) # Se contaron 6, O
print(cad[46]) # La letra reconocida es la M
print(cad[50]) # Se obtuvo la 4ta O


print("EJERCICIO N°11")
#              1         2         3         4
#    012345678901234567890123456789012345678901
cad="DIME CON QUIEN ANDAS Y TE DIRE QUIEN  ERES"


# De la cadena obtener lo sigueinte:
# Cantidad de la vocal E
# Cuantas veces se repite la cadena QUIEN
# La letra de la ubicacion -25
# La letra de la ubicacion -7

print(cad.count("E")) # Se repite 7 veces
print(cad.count("QUIEN")) # Se repite 2 veces
print(cad[-25]) # Es la letra D
print(cad[-7]) # Es  la letra N


print("EJERCICIO N°12")
#              1         2         3         4         5
#    01234567890123456789012345678901234567890123456789012345
cad="ANDA CON QUIEN TE ENSEÑE QUE LA VIDA NO ES COLOR DE ROSA"

# De la cadena obtener lo sigueinte:
# Cantidad de la vocal A
# La letra de la ubicacion -32
# La letra de la ubicacion 17

print(cad.count("A")) # Se repite 5 veces
print(cad[-32]) # Es la letra V
print(cad[17]) # Es  la vocal E


print("EJERCICIO N°13")
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
cad="QUE EL INTERES SEA MAS GRANDE QUE TU DEJADEZ, ASI APRENDERAS"

# De la cadena obtener lo sigueinte:
# Cantidad de la letra N
# La letra de la ubicacion -21
# La letra de la ubicacion -54

print(cad.count("N")) # Se repite 3 veces
print(cad[-21]) # Es la letra J
print(cad[-52]) # Es  la letra N


print("EJERCICIO N°14")
#              1         2         3         4
#    01234567890123456789012345678901234567890123
cad="LAS SUPERSTICIONES SON PARA LOS TONTOS DICEN"

# De la cadena obtener lo sigueinte:
# Cantidad de la vocal S
# La letra de la ubicacion 28
# La letra de la ubicacion -40

print(cad.count("S")) # Se repite 7 veces
print(cad[28]) # Es la letra L
print(cad[-40]) # Es  la letra S



print("EJERCICIO N°15")
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
cad="LA UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO HA SIDO LINCENCIADA"

# De la cadena obtener lo sigueinte:
# Cantidad de la vocal A
# La letra de la ubicacion 55
# La letra de la ubicacion 12
# Obtener la cadena GAHEL

print(cad.count("A")) # Se repite 7 veces
print(cad[-25]) # Es la letra D
print(cad[-7]) # Es  la letra N
print(cad[35] + cad[12] + cad[41] + cad[53] + cad[22])
