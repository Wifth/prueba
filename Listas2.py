lista = [7,6,5,4,3,2]
print(len(lista))
# Agregar elementos
lista.append(9) # Agrega al final el "9"
print(lista)
lista.insert(1,8) # Inserta el "8" en la posición #1
print(lista)
# Quitar elementos
del lista[3] # Elimina el "5" en la posición #3
print(lista)
lista.remove(4) # Elimina el primer valor "4"
print(lista)
# Info de elementos
print(lista.index(9))
# Reemplazo de elementos
lista[0] = 1
print(lista)