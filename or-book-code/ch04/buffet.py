foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')

# foods[2] = 'chicken' # TypeError: 'tuple' object does not support item assignment

print("Original foods:")
for food in foods:
    print(food)
    
foods = ('pizza', 'falafel', 'carrot cake', 'chicken', 'rice')

print("\nNew foods:")
for food in foods:
    print(food)