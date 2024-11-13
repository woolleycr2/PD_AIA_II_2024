import json

with open("config.json", "r") as my_file:
    dictionar = json.load(my_file)
    print(dictionar)

dictionar["TESTING"]["MAX_ERR"] = 0.01

with open("config.json", "w") as my_file:
    json.dump(dictionar, my_file)