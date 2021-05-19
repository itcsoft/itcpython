# Словарь(Dictionary)  внутри Списка(List)
banks = [
    {
        "name": 'Demir Bank',
        "address": 'ул. Курманжан-Датка 180а',
        "balance": 500000.00,
        "valuta": "KGS"
    },

    {
        "name": 'Optima Bank',
        "address": 'ул. Гапар Айтиев 6/1',
        "balance": 9654321,
        "valuta": "RUS"
    },

    {
        "name": 'KICB',
        "address": 'ул. Курманжан-Датка 202а',
        "balance": 978423.15,
        "valuta": "USD"
    },

    {
        "name": 'Dos-Credo Bank',
        "address": 'ул. Ленина 314а',
        "balance": 75542.65,
        "valuta": "EUR"
    }
]

# print(banks[0]['name'], banks[0]['address'])
# print(banks[1]['name'], banks[1]['address'])
# print(banks[2]['name'], banks[2]['address'])
# print(banks[3]['name'], banks[3]['address'])

# for bank in banks:
#     print(bank['name'], ':', bank['address'], bank['balance'])

for index in range(4):
    print(index + 1, ':', banks[index]['name'])

select_bank = int(
    input('Выберите Банк чтобы узнать баланс: ')
)

if select_bank < 5 and select_bank >= 1:
    print(
        'Баланс банка:', 
        banks[select_bank - 1]['balance'],
        banks[select_bank - 1]['valuta']
    )
else:
    print('Андай банк жок')


