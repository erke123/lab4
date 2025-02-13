def square_generator(n):
    
    for i in range(1, n+1):
       
       yield i**2
n = 10
square = square_generator(n)
for s in square:
    print(s)
