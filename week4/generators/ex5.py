def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
numbers = numbers_down_to_zero(n)
for number in numbers:
    print(number)