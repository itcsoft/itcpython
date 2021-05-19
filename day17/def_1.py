def calculator(san1, san2, suff):
    if suff == '*':
        print(san1 * san2)
    elif suff == '/':
        print(san1 / san2)
    elif suff == '-':
        print(san1 - san2)
    elif suff == '+':
        print(san1 + san2)


n1 = int(input('Сан 1: '))
n2 = int(input('Сан 2: '))
s = input('Эмне кылыш керек: ')
calculator(n1, n2, s)
