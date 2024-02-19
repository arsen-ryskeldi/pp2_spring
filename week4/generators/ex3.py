def divisible_by_3_and_4_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = 30
divisible_numbers = divisible_by_3_and_4_generator(N)
for number in divisible_numbers:
    print(number)