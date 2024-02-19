from datetime import datetime

x = datetime.now()

without = x.strftime("%Y-%m-%d %H:%M:%S")

print(without)