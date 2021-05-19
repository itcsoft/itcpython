# import module_0
# phone = input('Введите номер телефона: ')
# module_0.check_phone_number(phone)

# import module_0
# module_0.translate()

# fio = module_0.getFullName('Залкарбек', 'Асилов')
# print(fio)


# import mylib.calc.calculator as calculate
# from mylib.calc import calculator
# from mylib.calc import hello

# import mylib.calc as s

# s.calculator(10, 50, '+')
# s.hello()

# rstart = int(input('Введите начала рандома: '))
# rend = int(input('Введите конец рандома: '))

# print('Рандомное число: ', random.randint(rstart, rend))

import random 

mynum = int(input('Загадай число одно число я попробую найти это число через функцию ranint: '))

choose_num = random.randint(1, mynum + 10)

while choose_num != mynum:
    choose_num = random.randint(1, mynum + 10)
    print('Это число твое ?', choose_num)

if choose_num == mynum:
    print('Я нашел твое число чувак', choose_num)