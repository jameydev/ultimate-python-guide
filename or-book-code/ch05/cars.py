cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # should be all uppercase
        print(car.upper())
    else:
        print(car.title())