import datetime
x = input()
y = input()
data = "%Y-%m-%d %H:%M:%S"
data1 = datetime.datetime.strptime(x , data)
data2 = datetime.datetime.strptime(y , data)
data3 = data1-data2
data4 = data3.total_seconds()
print(data4)