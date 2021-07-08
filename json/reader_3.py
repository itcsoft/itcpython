import json

file = open('countries3.json', 'r')
countries = json.load(file)

while True:
    name = input('Введите имя страны: ')
    if name == 'exit':
        break
    for country in countries:
        if country['country'] == name:
            print(country['calling_code'])