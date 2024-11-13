import csv

A = {1, 7, 2, 8, 19, 1, -1, -5, -7, 0}
B = {0, 9, 1, -8, 7, 22, -5, -4, -3, 2}

with open("ex9.csv", "w") as my_file:
    writer_object = csv.writer(my_file, delimiter=',')
    writer_object.writerow(A)
    writer_object.writerow(B)

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(B.difference(A))


