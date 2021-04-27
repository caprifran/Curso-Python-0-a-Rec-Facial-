# Introducción a listas

array = ["futbol","Pc",18, 6, 19, [6, 7, 10.4], True, False, "Pc"]
print(array)
print("----------")
print(array[1])
print("----------")
print(array[5])
print("----------")
print(array[-1]) # Ultimo
print("----------")
print(array[-2])
print("----------")
print(array[0:3]) # == array[:3]
print("----------")
print(array[2:]) # Del 2 hasta el final
print("--------------------Funciones--------------------")

# Funciones

print("len(array) => ", len(array))

array.append(66)
print("append(66) => ", array)

array.insert(1, 88)
print("insert(1, 88) => ", array)

array.extend([1, 88, True, 100])
print("extend([1, 88, True, 100]) => ", array)

array2 = [200, 250, "hola"]
array3 = array + array2
print("array + array2 (concatenar) => ",array3)

print("Pc" in array) # Busca un valor dentro de un array y devuelve un booleano

print(array.index("Pc")) # Devuelve el indice de un valor determinado

print(array.count("Pc")) # Cuenta la cantidad de veces que se repite un determinado valor

array.remove("Pc") # Elimina el primer valor que coincida con el determinado
print(array)

array.clear() # Limpia todo el array
print(array)

array.reverse() # Invierte el orden del array
print(array)

array = [1, 2, 8, 5, -11]
array.sort() # Ordena un vector
print(array)

array.sort(reverse=True) # Ordena un vector e invierte su orden
print(array)



