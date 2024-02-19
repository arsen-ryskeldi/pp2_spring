from datetime import datetime

def differencee(date1, date2):
    difference = date2 - date1
    difference_seconds = difference.total_seconds()
    return difference_seconds

date1 = datetime(2023, 2, 19, 12, 30, 0)
date2 = datetime(2023, 2, 20, 10, 50, 0)

print(differencee(date1, date2))