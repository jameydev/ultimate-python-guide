motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
print(motorcycles)

popped_mc = motorcycles.pop()
print(motorcycles)
print(popped_mc)
