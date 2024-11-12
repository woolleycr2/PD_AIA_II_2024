student = {"nume": "Ionascu", "prenume": "Iulian", "varsta": 20, "an de facultate": 1, "universitate": "UGAL"}
print(student)
print(len(student))
print(student["nume"])
student["tara"] = "Romania"
student["an de facultate"] = 2
del student["varsta"]
print(student)