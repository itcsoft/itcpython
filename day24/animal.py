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