def print_square_parity(beginning, end):
    squares = [number ** 2 for number in range(beginning, end + 1)]

    odd_squares = [square for square in squares if square % 2 == 1]
    even_squares = [square for square in squares if square % 2 == 0]

    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)


print_square_parity(1, 5)