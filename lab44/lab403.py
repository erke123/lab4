def asd(n):
    for i in range(0, n+1):
        if i % 3 ==0 and i % 4 == 0:
            yield "yes"
        else:
            yield "no"
n = 30

for e in asd(n):
    print(e)