# # Home Work 1
# num1 = int(input()) # 3
# num2 = int(input()) # 5
# num3 = int(input()) # 4
# min = 0
# max = 0
# avarage = 0

# #MAX
# if num1 > num2 and num1 > num3:
#     max = num1

# if num2 > num1 and num2 > num3:
#     max = num2

# if num3 > num1 and num3 > num2:
#     max = num3

# # MIN
# if num1 < num2 and num1 < num3:
#     min = num1

# if num2 < num1 and num2 < num3:
#     min = num2

# if num3 < num1 and num3 < num2:
#     min = num3

# # AVARAGE
# if num1 > min and num1 < max:
#     avarage = num1

# if num2 > min and num2 < max:
#     avarage = num2

# if num3 > min and num3 < max:
#     avarage = num3


# print('MIN: ', min)
# print('MAX: ', max)
# print('AVARAGE: ', avarage)

# HOMEWORK 2
# a = int(input())

# if a % 2 == 0:
#     print('Четное число')
# else:
#     print('Не четное число')


# HOMEWORK 4
# Пользователь вводит логин и если логин "admin", то должно выйти сообщение "Добро пожаловать, программист!”, 
# если же логин "manager", то другая надпись - "Сайт приветствует руководство!". 
# В другом варианте должно выйти ещё одно сообщение "Программа завершила своё исполнение..."
# Пример:
# Ввод: 
# admin
# Вывод:
# Добро пожаловать, программист!
# Программа завершила своё исполнение...

login = input('YOur login: ')

if login == 'admin':
    print('Добро пожаловать прогер')
elif login == 'manager':
    print('Добро пож-вать Директор')
else: 
    print('Привет гость')