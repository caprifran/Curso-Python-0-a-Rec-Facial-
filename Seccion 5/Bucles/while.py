# Bucle while
import math

numero = 0
while numero < 20:
    print(numero)
    numero += 1
    
numero = int(input("Escriba un numero: "))

while numero < 0:
    print("Por favor ingrese un numero positivo")
    numero = int(input("Escriba un numero: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero)}")