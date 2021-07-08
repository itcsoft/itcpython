# Онлайн покупка через aliexpress
# Покупка Ноутбука Acer Predator 3500$
# AliExpress принимает только Visa и PayPal и SberPay
# Mastercard и Elcard не поддерживает

predator_sena = 3500 # Цена: Acer Predator 
balance = 5000 # Биздин баштапкы баланс
summa = int(input('Введите сумму: '))

print('Чтобы купить Acer Predator за 3500$: ')
sposob = (input('введит способ оплаты: ')).lower()

if sposob == 'mastercard':
    print('Извините мы не поддерживаем MasterCard')
elif sposob == 'elcard':
    print('Извините мы не поддерживаем Elcard')
elif sposob == 'visa' or sposob == 'paypal':
    creditcard = input('введите номер вашей карты: ')

    if len(creditcard) > 4 or len(creditcard) < 4:
        print('Некорректный номер карты ??')
        quit()

    if predator_sena > balance:
        print('У вас недостаточно средтсв не хватает для покупки')
    else:
        print('Вы можете совершить покупку.')
        print('Поздравляем вы купили Acer Predator')
        print('Остаток', balance - summa)
else:
    print('Такой вид карты не поддерживается')

