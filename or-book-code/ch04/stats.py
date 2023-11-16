digits = list(range(10))

print('\nDigits: ')
for digit in digits:
    if (digit == digits[-1]):
        print(digit)
    else:
        print(digit, end=', ')
        
print('\nMaximum: ', max(digits))
print('Minimum: ', min(digits))
print('Sum: ', sum(digits))