# Programa 1.10 Revisar si puedes ver una película en Netflix. la condición para esto es que seas mayor de edad y que hayas comprado la película agregar, gracias por usar Netflix 
# Fecha: 2024/10/25
# Elaborado por: Jazmin Macias Sabas 
edad = int(input("¿Cuantos años tienes?"))
if edad >=18:
    compra = int(input("¿Compraste la película?"))
    if compra ==1:
        print("Puede ver la película")
else:
    print("Vete a hacer la tarea")
