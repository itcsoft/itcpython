
# Автосалон Bootcamp
car1 = {
    'model': 'Honda Fit 2',
    'year': '2008',
    'vol': 1.6,
    'color': 'silver',
    'price': 5500.0,
    'max_speed': 260
}
car2 = {
    'model': 'Mercedes SLG 63',
    'year': '2016',
    'vol': 4.0,
    'color': 'black',
    'price': 142000.0,
    'max_speed': 350
}
car3 = {
    'model': 'Matiz 2',
    'year': '2008',
    'vol': 1.4,
    'color': 'blue',
    'price': 3500.0,
    'max_speed': 180
}

print('Добро пожаловать в Автосалон Bootcamp.')
print('Машины в наличии: ')
print('1: ', car1['model'])
print('2: ', car2['model'])
print('3: ', car3['model'])

select_car = int(input('Какую машину выбрать: '))

if select_car == 1:
    carKey = input('Какую харак. хотите увидеть: ')
    if car1.get(carKey) != None:
        print(carKey, car1[carKey])
    else:
        print('Такой харак. у машины нет')

if select_car == 2:
    carKey = input('Какую харак. хотите увидеть: ')
    if car2.get(carKey) != None:
        print(carKey, car2[carKey])
    else:
        print('Такой харак. у машины нет')

if select_car == 3:
    carKey = input('Какую харак. хотите увидеть: ')
    if car3.get(carKey) != None:
        print(carKey, car3[carKey])
    else:
        print('Такой харак. у машины нет')
    
   