def change(x):
    a = 10
    x[0] = a + x[0]

x = [5]
print(x)
change(x)
print(x)