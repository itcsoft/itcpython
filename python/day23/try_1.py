cars = {
    'Toyota': 1999,
    'Hyndai': 2006,
    'Kia': 2008,
    'Mercedes': 2005,
    'Renault': 2018,
    'Matiz': 2016,
    'Porter Electro': 2021
}

try:
    car_file = open('carss.txt', 'w')
    for key, value in cars.items():
        car_file.writelines(key + ',' +str(value) + '\n')
except FileNotFoundError:
    print('Не могу найти файл')