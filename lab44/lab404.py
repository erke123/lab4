def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = 10
b= 20

asd = squares(a, b)
for i in asd:
    print(i)