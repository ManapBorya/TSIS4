def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Test the generator with a for loop
a = 2
b = 5

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)