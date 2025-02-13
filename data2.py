import datetime
x = datetime.datetime.now()
d = x - datetime.timedelta(days= 1)
c = x + datetime.timedelta(days= 1)
print(d,x,c)