import datetime

a = datetime.datetime.now() - datetime.timedelta(days = 1)
b = datetime.datetime.now() - datetime.timedelta(days = 0)
c = datetime.datetime.now() + datetime.timedelta(days = 1)

print(a)
print(b)
print(c)