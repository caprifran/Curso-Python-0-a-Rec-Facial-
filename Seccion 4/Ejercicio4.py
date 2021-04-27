# Ejercicio 4

'''
Crear un programa que simule un cajero
automático con un saldo inicial de $2000, con
el siguiente menú:
1. Ingreso de dinero
2. Retirar dinero
3. Mostrar dinero
4. Salir
'''

saldo = 2000
print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion = int(input("Elija una opcion: "))

if seleccion == 1:
    ingreso = float(input("Dinero a ingresar: "))
    saldo += ingreso
    print(f"Su nuevo saldo es de ${saldo}")
elif seleccion == 2:
    retiro = float(input("Dinero a retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= retiro
        print(f"Su nuevo saldo es de ${saldo}")
elif seleccion == 3:
    print(f"Su saldo es de {saldo}")
elif seleccion == 4:
    print("Fin")
else:
    print("Opcion invalida")    
