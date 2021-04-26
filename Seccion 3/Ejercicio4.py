# Ejercicio 4
'''
Obtener el precio final que se tiene que pagar
si se aplica el 36% de desceunto del total de la
compra
'''

precioInicial = float(input("Ingrese el precio: "))
descuento = precioInicial * 0.36
precioFinal = precioInicial - descuento

print(f"El precio final es: ${precioFinal:.2f}")
