n = int(input())
def generater(n):
    even = []
    for i in range(0 , n+1, 2):
        even.append(i)

    return even
e = generater(n)
for i in range(len(e)):
    if i != len(e) -1:
        print(e[i], end=" , ")
    else:
        print(e[i])
