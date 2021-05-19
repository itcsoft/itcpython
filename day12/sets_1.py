# names = ['zalkar', 'zalkar', 'beka', 'tom']

# names = {
#     'zalkar', 
#     'zalkar', 
#     'beka', 
#     'beka', 
#     'tom'
# }
# print(names)

# vegetables = {
#     'картошка',
#     'картошка',
#     'картошка',
#     'картошка',
#     'картошка',
#     'картошка',
#     'морковь',
#     'морковь',
#     'морковь',
#     'морковь',
#     'лук'
# }
# print(vegetables)


# emails = [
#     'zalkar@gmail.com',
#     'zalkar@gmail.com',
#     'zarlyk@gmail.com',
#     'nur@gmail.com',
#     'beka@gmail.com',
#     'erlan@gmail.com',
#     'amantur@gmail.com',
#     'amantur@gmail.com',
#     'amantur@gmail.com',
# ]

# emails = set(emails) 
# # {'zalkar@gmail.com', 'nur@gmail.com', ...}

# for email in emails:
#     print('На почту', email, 'отправлен приглашение на вечеринку')

# friends = {
#     'Бектур',
#     'Бектур',
#     'Темирлан',
#     'Жаныбек',
#     'Нурбек',
#     'Калыс',
#     'Калыс'
# }

# print(friends)

#2
# products = {
#     'сахар'
# }
# print(products)
# products.add('чай')
# products.add('соль')

# product = ''
# for i in range(5):
#     product = input('Сатып алына турган продукт: ')
#     products.add(product.lower())

# print(products)

#3

# products = {
#     'сахар',
#     'чай',
#     'нан',
#     'суу',
#     'макарон'
# }
# print('ДО УДАЛЕНИЯ: ', products)
# products.remove('суу')
# print('ПОСЛЕ УДАЛЕНИЯ:', products)

# 4
# products = {
#     'сахар',
#     'чай',
#     'нан',
#     'суу',
#     'макарон'
# }
# print('ДО ОЧИСТКИ: ', products)
# products.clear()
# print('ПОСЛЕ ОЧИСТКИ:', products)


# products = {
#     'сахар',
#     'чай',
#     'нан',
#     'суу',
#     'макарон'
# }

# fruits = {
#     'apple',
#     'watermelon'
# }

# print('ДО: ', products)

# # Обьединяет два множества
# products.update(fruits)

# print('ПОСЛЕ:', products)


# company1 = { 'apple', 'microsoft', 'kia', 'honda', 'Sony' }
# company2 = { 'LG', 'panasonic', 'microsoft', 'apple' }
# company3 = { 'Sony', 'Toyota', 'BMW', 'apple' }

#difference_company = company1.difference(company2)
#print(difference_company)
# intersection = company1.intersection(company2)
# print(intersection)

# company1.intersection_update(company2)
# print(company1)
# company1.intersection_update(company3)
# print(company1)


# company1 = { 
#     'apple', 
#     'microsoft', 
#     'kia', 
#     'honda' 
# }
# company1.pop()
# print(company1)


users = { 
    'Залкарбек',
    'Зарлык',
    'Амантур',
    'Tima',
    'Том',
    'Mike',
    'John',
    'Rik',
    'Krishna',
    'Jobs',
    'Бекзат',
    'Steve',
    'Rocki',
    'Бекгазы'
}

# mest_1 = users.pop()
# print(mest_1)

# prizmesto = int(input('введите количество призовых мест: '))

# for i in range(prizmesto):
#     input('место получает...')
#     print(i, 'место получает...')
#     print(i+1, 'место:', users.pop())


# pwrds = set()
# pwrd = ''
# numpwrd = int(input('Канча турлуу пароль киргизесиз: '))

# for i in range(numpwrd):
#     pwrd = int(input('Пароль киргизиниз: '))
#     pwrds.add(pwrd)

# for i in range(numpwrd):
#     print(i+1, '- пароль: ', pwrds.pop())




