
magics = {}
enemy = {
    'dragon': 30
}

magic_file = open('magic.txt', 'r')
magic_array = magic_file.readlines()

for cur_magic in magic_array:
    magic_striped = cur_magic.strip()
    magic_splitted = magic_striped.split(',')
    magics[magic_splitted[0]] = float(magic_splitted[1])


print('Ваш противник:', enemy)
print('Выберте магию')

print('1.Удар огнем, 5')
print('2.Водопад, 3')
print('3.Удар молнией, 4')
print('4.ExpetusPatronus, 6')
print('5.Чидори, 8')
print('6.Удар ногой, 1')
print('7.Сальто удар, 2')
print('8.Топот, 0.5')
a = int(input('Выберите Магию: '))
if a == 1:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Удар огнем']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])

elif a == 2:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Водопад']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a == 3:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Удар огнем']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a == 4:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['ExpetusPatronus']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a == 5:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Чидори']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a== 6:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Удар ногой']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a == 7:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Сальто удар']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
elif a == 8:
    print('Война началась')
    while enemy['dragon'] > 0:
        u = magics['Топот']
        enemy['dragon'] = enemy['dragon'] - u
        print('XP врага:', enemy['dragon'])
    print('Вы победили Жизнь врага: ', enemy['dragon'])
else:
    print('Дебил такой Магии нету')









# while enemy['dragon'] > 0:
#     udar = input('Выберите удар: ')
#     u = magics[udar]
#     enemy['dragon'] = enemy['dragon'] - u
#     print('XP врага:', enemy['dragon'])

# print('Вы победили Жизнь врага: ', enemy['dragon'])