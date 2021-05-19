# Функция это блок операторов которые можно вызывать где угодно
#print('Разница: {}'.format(san1 - san2))

# def summa(num1, num2):
#     print('----------')
#     print('Сумма: {}'.format(num1 + num2))
#     print('----------')


# def mines(num1, num2):
#     print('----------')
#     print('Айырмасы: {}'.format(num1 - num2))
#     print('----------')


# san1 = int(input('Сан 1: '))
# san2 = int(input('Сан 2: '))

# summa(san1, san2)
# mines(san1, san2)

def salamdash(lang):
    if lang == 'en':
        print('Hello Hi How are You')
        print('Maybe go to learn Python')
    elif lang == 'kg':
        print('Ассалоому Алейкум. Иштер кандай ?')
        print('Python уйронгону кеттикби')
    elif lang == 'ru':
        print('Добрый вечер')
        print('Поехали бухат')


l = input('Кайсы тилде саламдашайын: ')
salamdash(l)