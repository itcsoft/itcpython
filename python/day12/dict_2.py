
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
    print('Модель:', car1['model'])
    print('Год:', car1['year'])
    print('Обьем:', car1['vol'])
    print('Цвет:', car1['color'])
    print('Цена:', car1['price'])
    print('Макс скорость:', car1['max_speed'])

if select_car == 2:
    print('Модель:', car2['model'])
    print('Год:', car2['year'])
    print('Обьем:', car2['vol'])
    print('Цвет:', car2['color'])
    print('Цена:', car2['price'])
    print('Макс скорость:', car2['max_speed'])

if select_car == 3:
    print('Модель:', car3['model'])
    print('Год:', car3['year'])
    print('Обьем:', car3['vol'])
    print('Цвет:', car3['color'])
    print('Цена:', car3['price'])
    print('Макс скорость:', car3['max_speed'])