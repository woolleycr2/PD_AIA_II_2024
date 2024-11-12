tuplu = (1, "xyz", 3.14, False, [4,6])
print(tuplu)
print(len(tuplu))
tuplu_nou = tuplu[:3]
#tuplu_nou[0] = 10 - TypeError: 'tuple' object does not support item assignment
lista = list(tuplu_nou)
print(lista)