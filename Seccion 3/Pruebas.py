print("Hola Mundo")
print('Soy Franco')

numero1 = 50
numero2 = 50.6

print(numero1)
print(type(numero1))

print(numero2)
print(type(numero2))

palabra = 'Hola de nuevo'

print(palabra)
print(type(palabra))

dato1 = True
dato2 = False

print(dato1)
print(type(dato1))

print(dato2)
print(type(dato2))

n1 = 120
n2 = 12.8

suma = n1 + n2
print('Resultado suma: ', suma)

resta = n1 + n2
print('Resultado resta: ', resta)

multiplicacion = n1 * n2
print('Resultado multiplicación: ', multiplicacion)

potencia = n1 ** n2
print('Resultado potencia: ', potencia)

division = n1 / n2
print('Resultado división: ', division)

divisionRedondeada = n1 // n2
print('Resultado división redondeada: ', divisionRedondeada)


modulo = n1 % n2
print('Resultado modulo: ', modulo)

resultOp = (n1 + n2 * 5) / 12
print('Resultado operación: ', resultOp)

dato = 60
print(dato)

dato = "Cambio de valor"
print(dato)

dato = 10.8
print(dato)

# Este es un comentario
# Segunda linea
'''
Fragmento de comentarios multilinea
asdasd
asd
asd
a
sd
asd 
'''

# Operacion aritmetica
r = (5 + 9 / 3) ** 2
print(r)

# Operadores relacionales / comparacion
# == igual que
# != distinto que
# < menor que 
# <= menor o igual que 
# > mayor que 
# >= mayor igual que

r1 = 50 == 100
r2 = 100 == 100
print('50 == 100 =>', r1)
print('100 == 100 =>', r2)

r1 = 50 != 100
r2 = 100 != 100
print('50 != 100 =>', r1)
print('100 != 100 =>', r2)

r1 = 50 < 100
r2 = 100 < 100
print('50 < 100 =>', r1)
print('100 < 100 =>', r2)

r1 = 50 <= 100
r2 = 100 <= 100
r3 = 101 <= 100
print('50 <= 100 =>', r1)
print('100 <= 100 =>', r2)
print('101 <= 100 =>', r3)

r1 = 50 > 100
r2 = 101 > 100
print('50 > 100 =>', r1)
print('101 > 100 =>', r2)

r1 = 50 >= 100
r2 = 100 >= 100
r3 = 105 >= 100
print('50 >= 100 =>', r1)
print('100 >= 100 =>', r2)
print('105 >= 100 =>', r3)

# Operadores lógicos
# and Se cumple a y b
# or  Se cumple a o b
# not No a

a = 30
b = 40
c = 50

r = ((a < b) and (b < c))
print('(a < b) and (b < c) =>', r)
r = ((a > b) and (b < c))
print('(a > b) and (b < c) =>', r)

r = ((a > b) or (b < c))
print('(a > b) or (b < c) =>', r)
r = ((a > b) or (b > c))
print('(a > b) or (b < c) =>', r)

# Operadores de asignación
c = 0
c += 10
c -= 5
c *= 3
c /= 5
c **= 3
c %= 3
print(c)

# Salidas de datos
app = "flutter"
proyecto = "conFlu"
print(f"se hara en {app} se llamara {proyecto}")

# Entradas de datos 
cadena = input("¿Comó se llama tu proyecto?: ")
print(f"Tu proyecto se llama {cadena}")

cadena = float(input("¿Qué version es?: "))
print(f"Version: {cadena + 1}")


