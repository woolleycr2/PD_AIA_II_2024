#8c_alternative: import math
import csv

def valoare_maxima(list_or_tuple: list | tuple):
    if not isinstance(list_or_tuple, tuple | list):
        raise TypeError("Parameter must be a list or a tuple")
    if isinstance(list_or_tuple, tuple):
        tuple_to_list =  list(list_or_tuple).copy()
        tuple_to_list.sort()
        return tuple_to_list[-1]
    else:
        list_sorted = list_or_tuple.copy()
        list_sorted.sort()
        return list_sorted[-1]

def suma(list_1, list_2: list):
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        raise TypeError("Both parameters must be lists")
    list_3 = []
    if len(list_1) != len(list_2):
        return list_3
    else:
        for i in range(len(list_1)):
            list_3.append(list_1[i] + list_2[i])
        return list_3

def factorial(intreg: int):
    if not isinstance(intreg, int):
        raise TypeError("Parameter must be an integer")
    else:
        result = 1
        for i in range(1, intreg + 1):
            result *= i
        return result
        #8c_alternative: return(math.factorial(intreg))

def export_csv(lista_csv: list, nume_fisier: str):
    if not isinstance(lista_csv, list):
        raise TypeError("Parameter must be a list")
    elif not isinstance(nume_fisier, str):
        raise TypeError("Parameter must be a string")
    else:
        with open(nume_fisier, "a") as my_file:
            writer_object = csv.writer(my_file, delimiter=',')
            writer_object.writerow(lista_csv)

def rezistente_paralel(lista_valori: list):
    suma_valori = 0
    if not isinstance(lista_valori, list):
        raise TypeError("Parameter must be a list")
    else:
        for i in lista_valori:
            suma_valori += 1 / i
    return 1 / suma_valori

lista_1 = [6, 3, 2, 12, 1, 3]
lista_2 = [3, 2 ,1 ,5 ,6 ,7]
tuplu = (1, 4, 5, 2 ,7, 16, 3)
nume_fisier_8d = "ex8d.csv"
print(valoare_maxima(lista_1))
print(valoare_maxima(tuplu))
print(suma(lista_1, lista_2))
print(factorial(3))
export_csv(lista_1, nume_fisier_8d)
print(rezistente_paralel(lista_1))

