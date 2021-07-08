password = input('Введите пароль: ')

if len(password) < 5:
    print('Ваш пароль слишком слабый')

elif len(password) > 5 and len(password) <= 7:
    print('Ваш пароль средний')

elif len(password) >= 8:
    print('Ваш пароль сложный')