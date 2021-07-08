

password = input('Введите пароль: ')

if len(password) < 4:
    print('Пароль очень легкий или не ввели!!')
elif len(password) >= 4 and len(password) <= 6:
    print('Пароль, средний!!')
elif len(password) >= 8:
    print('Хороший пароль))')