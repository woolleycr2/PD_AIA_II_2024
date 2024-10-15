x = 1
s = 0
while x <= 100:
    s = s + (1 / x ** 2)
    x = x + 1
print(s)

x = 1
s = 0
while x <= 5:
    s = s + (x ** 2 - x)
    x = x + 1
print(s)

x = 4
s = 0
while x <= 15:
    s = s + ((2 ** (x + 1)) / (x - 1))
    x = x + 1
print(s)