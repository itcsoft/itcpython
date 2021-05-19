
class AviaSales:
    def __init__(self):
        self.tickets = {
            'Moscow': {
                'data': '12.05.2021',
                'price': 47_000
            },
            'Dubai': {
                'data': '13.05.2021',
                'price': 97_000
            },
            'Turkey': {
                'data': '27.05.2021',
                'price': 27_000
            }
        }

    def get_biletter(self, kuda):
        if kuda in self.tickets:
            print(
                kuda,'\n',
                'Дата: ',
                self.tickets[kuda]['data'],
                 '\n',
                'Цена: ',
                '',
                '\n',
                self.tickets[kuda]['price']
            )
        else:
            print('Билеты на:', kuda, 'нет')

samturAvia = AviaSales()

mesto = input('Куда хотите поехать ?: ')

samturAvia.get_biletter(mesto)