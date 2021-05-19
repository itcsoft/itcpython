
# Обьекты (Классы)
# class Tiger:
#     name = 'Шерхан'
#     weight = 400
#     age = 5
#     color = 'ОранжевоЧерныйБелый'
#     speed = 50
#     power = 99

# tigr = Tiger()
# tigr2 = Tiger()
# tigr2.name = 'Мурсик'
# tigr2.weight = 300

# print(tigr.name)
# print(tigr2.name)
# print(tigr2.weight)


# class Human:
#     name = ''
#     color = ''
#     rassa = ''
#     gender = ''
#     weight = ''
#     age = ''
#     hair = ''
#     hair_color = ''
#     def to_walk(self):
#         print(self.name, 'Баса алат')
    
#     def to_speak(self, word, word2):
#         print(self.name, 'govorit', word, word2)


# belek = Human()
# belek.name = 'Белек'
# belek.color = 'Будай цветтуу'
# belek.rassa = 'Кыргыз'

# belek.to_walk()
# belek.to_speak('Салам кандай ?', 'Жакшы озун')
# ai_92 = 49.50
# ai_95 = 51.50

# ОБьект Машина
# class Car:
#     rasxod_100 = 12
#     def __init__(self, name, year, color, volume):
#         self.name = name
#         self.year = year
#         self.color = color
#         self.volume = volume
    
#     def get_volume(self):
#         print('Мой обьем:', self.volume)

#     def get_rasxod(self, km):
#         r = (km / 100) * self.rasxod_100
#         return r

#     def get_rasxod_price(self, km):
#         r = self.get_rasxod(km)
#         print('92 На', km,'km', r * ai_92, 'som')
#         print('95 На', km,'km', r * ai_95, 'som')

# mycar = Car(
#     name = 'Matiz 1', 
#     year = 2000,
#     color = 'Белый',
#     volume = 3.5
# )

# mycar.get_volume()
# mycar.get_rasxod(145)
# mycar.get_rasxod_price(145)

class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type']
        self.speed = kwargs['speed']

    def get_speed(self):
        print('Бегает {} km в час'.format(self.speed))

    def get_full_time(self, km):
        print(km / self.speed)

name = input('Введите имя животного: ')

leopard = Animal(
    name = name,
    type = 'Кошачий',
    speed = 90
)

leopard.get_speed()
leopard.get_full_time(80)