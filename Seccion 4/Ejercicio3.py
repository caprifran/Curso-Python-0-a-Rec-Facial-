# Ejercicio 3

'''
Crea un programa que compare dos nombres, 
verificar si hay coincidencia o no, si es que
ambos nombres comienzan con la misma letra
o si terminan con la misma letra
'''

nombre1 = input("nombre 1: ")
nombre2 = input("nombre 2: ")

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia")