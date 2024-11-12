with open("lista_cumparaturi.txt", "r") as my_file_r:
    print(my_file_r.read())
    with open("lista_cumparaturi.txt", "a") as my_file_a:
        my_file_a.write("\nLegume")

with open("lista_cumparaturi.txt", "r") as my_file_r:
    with open("lista_cumparaturi_actualizata.txt", "w") as my_file_x:
        my_file_x.write(my_file_r.read())
        print("S-a creat/actualizat fisierul 'lista_cumparaturi_actualizata.txt'.")