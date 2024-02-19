def squares_generator(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = 3
b = 7
squares = squares_generator(a, b)
for square in squares:
    print(square)