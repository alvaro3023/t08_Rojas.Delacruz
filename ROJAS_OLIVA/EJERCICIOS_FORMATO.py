print("EJERCICIO N°1")
#               1         2
#     0123456789012345678901
cad1="#N° CLIENTE: #CAJERO: "
cad2="Alvaro Mauricio"
cad3="TOTAL: {}"
cad4="#PEDIDO #CANTIDAD #COSTO"
cad5="°PAN °TARRO DE LECHE"
nro="1"
msg="{0:#^44}"     # Mostrar mensaje centrado y con #
msg2="{0:*^26}"
msg3="{0:*^44}"
monto1_str="2.00"
monto2_str="3.60"

print("#"*(44))
print(msg.format("BOLETA DE VENTA"))
print("#"*(44))
print(cad1[:12] + "  " + cad1[13:30])
print("#"*(44))
print(cad4[:7] + "       " + cad4[8:17] + "         " + cad4[18:24])
print(cad5[:4]  + monto1_str.rjust(33).zfill(3))
print(cad5[5:20] + nro.rjust(5).zfill(2) + monto2_str.rjust(17).zfill(3))
print(msg2.format("") + cad3.format("5.60"))
print("_ "*22)
print(msg3.format("GRACIAS POR SU PREFERENCIA"))




print("EJERCICIO N°2")
#               1         2
#     01234567890123456789012345
cad1="CEVICHERIA   SEÑOR DELFIN "
cad2="#COMENSAL: #AZAFATA:"
cad3="JOSUE MARIELA"
cad4="#PEDIDO  #COSTO"
cad5="#ARROZ CON MARISCOS #REFRESCO DE LIMA #OCOPA "
cad6="#TOTAL: {}"
monto1_str="15.60"
monto2_str="2.50"
monto3_str="5.50"


print("#"*44)
print("#"*(9) + cad1[:] + "#"*(9))
print("#"*44)
print(cad2[:10]+ " " + cad3[:5] + "  " + cad2[10:20] + cad3[5:13])
print(cad4[:7] + "                 " + cad4[8:15])
print(cad5[:18] + "        " + monto1_str.zfill(4))
print(cad5[20:37] + "          "  + monto2_str.zfill(4))
print(cad5[38:44] + "                     " + monto3_str.zfill(3))
print("_"*44)
print(cad6.format("                  23.60"))

print("EJERCICIO N°3")
#               1         2         3         4         5
#     01234567890123456789012345678901234567890123456789012
cad1="EIRL  UNIKE"
cad2="#PRODUCTO #COSTO"
cad3="#LABIAL NEGRO: #SOMBRAS: #LAPIZ NEGRO: #BASE: #RUBOR:"
cad4="TOTAL: {}"
msg="{0:*^40}" # Mostrar mensaje centrado y con asteristicos

monto1_str="8.90"
monto2_str="15.50"
monto3_str="6.90"
monto4_str="35.50"
monto5_str="10.50"

print("#"*(44))
print("#"*16 + cad1[:11] + "#"*17)
print("#"*(44))
print(cad2[:9] + "                         " + cad2[9:16])
print(cad3[:14] + monto1_str.zfill(3).rjust(26)  )
print(cad3[15:24]+ monto2_str.zfill(4).rjust((31)))
print(cad3[25:38]+ monto3_str.zfill(4).rjust((27)))
print(cad3[39:45] + monto4_str.zfill(4).rjust(34))
print(cad3[46:] +  monto5_str.zfill(4).rjust(33))
print("_ "*22)
print(cad4.format("                            77.30"))
print(msg.format("GRACIAS POR SU COMPRA"))


print("EJERCICIO N°4")
#               1         2         3         4         5
#     0123456789012345678901234567890123456789012345678901234567
cad1="#COMBUSTIBLE #TIPO DE GASOLINA #GALON #COSTO #TIPO DE PAGO"
cad2="°GASOLINA °PREMIUM °MEDIO °TARJETA"
cad3="TOTAL: {}"
msg="{0:#^70}"     # Mostrar mensaje centrado y con #
msg2="{0:*^70}"
monto1_str="50.90"

print("#"*(70))
print(msg.format("GRIFO REPSOL IERL"))
print("#"*(70))
print(cad1[:12] + "  " + cad1[13:30] + "   " + cad1[31:37] + "   " + cad1[38:44] + "   " +  cad1[45:])
print(cad2[:9] + "        " + cad2[10:18] + "         " + cad2[19:25] + "   " + monto1_str.zfill(4) + "    " + cad2[26:34])
print("_ "*35)
print(msg2.format("EL MEJOR COMBUSTIBLE PARA SU CARRO"))

print("EJERCICIO N°5")
#               1         2
#     0123456789012345678901
cad1="#N° CLIENTE: #CAJERO: "
cad2="Alvaro Mauricio"
cad3="TOTAL: {}"
cad4="#PEDIDO #CANTIDAD #COSTO"
cad5="°PAN °TARRO DE LECHE"
nro="1"
msg="{0:#^44}"     # Mostrar mensaje centrado y con #
msg2="{0:*^26}"
msg3="{0:*^44}"
monto1_str="2.00"
monto2_str="3.60"

print("#"*(44))
print(msg.format("BOLETA DE VENTA"))
print("#"*(44))
print(cad1[:12] + "  " + cad1[13:30])
print("#"*(44))
print(cad4[:7] + "       " + cad4[8:17] + "         " + cad4[18:24])
print(cad5[:4]  + monto1_str.rjust(33).zfill(3))
print(cad5[5:20] + nro.rjust(5).zfill(2) + monto2_str.rjust(17).zfill(3))
print(msg2.format("") + cad3.format("5.60"))
print("_ "*22)
print(msg3.format("GRACIAS POR SU PREFERENCIA"))
