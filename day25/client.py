import crypt

class Client:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.__password = password
        #self.set_password(password)
    
    def set_password(self, password):
        if len(password) < 8:
            print('пароль слишком легкий')
        else:
            self.__password = password

    def get_password(self):
        return 'шифрованный'
    
    def raw_password(self):
        print('никому не рассказывайте пароль')
        return self.__password
        


# Интернет магазин bootcamp
# наш клиент
turgun = Client('Тургунбай', 'turgun', '1' )


# Меняем пароль клиента. Принимает только сложные пароли
# turgun.set_password('12345678')

# получаем зашифрованный пароль. Публичный доступ
#print(turgun.get_password())

# получаем голый пароль только разработчики имеют на это право!!! Приватный доступ
# print(turgun.raw_password())