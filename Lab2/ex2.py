lista = [10, 6, 3, 4, 1, 2, 5, 7, 9]
lista_g = [1,2,3]
print(lista)
print(type(lista))
lista.append(11)
lista.insert(7, 8)
print(len(lista))
lista.sort()
lista.extend(lista_g)
lista.pop(0)
lista.pop(-1)
print(lista)

