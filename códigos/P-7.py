# Programa 7 Calcula el área y el perímetro de un círculo 
# ingresando el valor del radio por el usuario 
# Fecha: 2024/10/15
# Elaborado por: Jazmin Macias Sabas 
#------------------------------------------------------------------#
radio = float(input("ingresa el valor del radio:"))
areacirculo = 3.1416 * radio ** 2
perimetrocirculo =  3.1416 * 2 * radio 

print("el valor del área es:" + str(areacirculo))
print("el valor del perimetro es:" + str(perimetrocirculo))
