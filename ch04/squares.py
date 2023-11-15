squares = []
for value in range(1, 11):
    squares.append(value ** 2)

for square in squares:
    # print the last element without comma
    if (square == squares[-1]):
        print(square) 
    else:
        print(square, end=', ') # end=', ' is used to print the output in one line