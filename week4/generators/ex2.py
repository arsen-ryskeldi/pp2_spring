def even_numbers_generator(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i

N = int(input())

even_numbers = even_numbers_generator(N)
for number in even_numbers:
    print(number, end=", ")