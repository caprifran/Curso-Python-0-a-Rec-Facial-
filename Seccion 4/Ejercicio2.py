# Ejercicio 2
'''
Crear un programa que pida 3 números y
determine cual es el mayor
'''

n1 = int(input("Ingrese el numero: "))
n2 = int(input("Ingrese el numero: "))
n3 = int(input("Ingrese el numero: "))

if n1 >= n2 and n1 >= n3:
    print(f"EL numero mayor es {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"EL numero mayor es {n2}")
elif n3 >= n1 and n3 >= n2:
    print(f"EL numero mayor es {n3}")
