#  Programa 8 Realice un programa que calcule el número de minutos, horas y meses dado el número de días por el usuario 
# Fecha: 2024/10/16
# Elaborado por: Jazmin Macias Sabas 
Días = float(input("Ingrese el número de días:"))
Horas = Días * 24
Minutos = Horas * 60
Meses = Días / 30 
print("Días:" + str(Días))
print("Horas::" + str(Horas))
print("Minutos::" + str(Minutos))
print("Meses::" + str(Meses))
