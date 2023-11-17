numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinals = ['st', 'nd', 'rd', 'th']

index = 0
for number in numbers:
    if index < 3:
        print(f"{number}{ordinals[index]}")
    else:
        print(f"{number}{ordinals[3]}")
    
    index += 1