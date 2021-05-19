def kvadrat(number):
    if number < 0:
        print('Он сан бер') 
    else:
        number = number * number
        print(number)


def divide(number1, number2):
    if number2 == 0:
        print('Нольго болсо болбойт')
    else:
        print(number1 / number2)


divide(10, 0)