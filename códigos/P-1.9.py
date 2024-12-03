# Programa 1.9 Programa que calcule el costo total de un número de artículos si: Son 3 artículos o menos precio unitario: $45.00. Más de 3 artículos precio unitario: $30. al final mostrar un mensaje 
# Fecha: 2024/10/25
# Elaborado por: Jazmin Macias Sabas 
cantidad = int(input("¿Cuantos articulos compro? "))
if cantidad>3:total = cantidad * 30
else: total = cantidad * 45
print("El total a pagar es: $" + str(total))
print("Saludos")
