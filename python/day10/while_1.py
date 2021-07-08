
password = 1213
mepassword = 0
trycount = 5

while mepassword != password and  trycount > 0:
    mepassword = int(input('Ваш пароль: '))
    if mepassword != password:
        trycount = trycount - 1
        print('У вас осталось ', trycount, 'попыток')
        print('Че ты тупишь Человек.')
    else:
        print('ОК Молодец Человек.')
