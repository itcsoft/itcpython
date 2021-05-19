try:
    a = int(input('Введите число 1: '))
    b = int(input('Введите разделитель числа: '))
    z =  a / b * jok
    print(z)
except NameError:
    print('Неправильные переменные')
except ValueError:
    print('ОШибка введите число а не текст')
except ZeroDivisionError:
    print('ОШибка делить на ноль нельзя')
except:
    print('Ошибка что то не так')
