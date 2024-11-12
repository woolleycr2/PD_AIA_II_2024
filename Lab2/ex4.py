my_set = {2, 4, 6, 8, 10}
print(my_set)
my_set.add(9)
my_set.add(2) # elementul 2 nu este adaugat deoarece tipul de date set nu poate avea 2 elemente cu aceeasi valoare
my_set.remove(2)
my_set.pop()
elemente_aditionale = {11, 12, 13}
my_set.update(elemente_aditionale)
print(my_set)

