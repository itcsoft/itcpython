def calculator(san1, san2, suff):
    if suff == '*':
        print(san1 * san2)
    elif suff == '/':
        if san2 == 0:
            print('На ноль делить нельзя')
            quit()
        print(san1 / san2)
    elif suff == '-':
        print(san1 - san2)
    elif suff == '+':
        print(san1 + san2)


def hello():
    print('HEllo Python')