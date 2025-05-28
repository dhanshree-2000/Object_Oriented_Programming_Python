def print_squares(n):
    yield n*n


n = 10
print(f"Squares up to {n}:")
for square in range(n):
    square = print_squares(square)
    print(next(square))