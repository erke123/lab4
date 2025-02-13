import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
s = (n * a**2)
p = math.pi
np = p/n
cotan_x = 1 / math.tan(np)

ss = (s * cotan_x)/ 4
print(math.trunc(ss))