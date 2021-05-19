# 0-0 Например:
# username = 'Tom'
# lastname = 'Jonson'
# print('ИМЯ: {0}'.format(username))
#print('Ages: {0}years old {1} {2}'.format(24, 36, 94))


# 0-1 Например:
# num1 = 36
# num2 = 72
# print('{0} + {1} = {2}'.format(num1, num2, num1 + num2))


# 0-2 Например:
# message = 'Whats your {} and {}'.format('name', 'age')
# print(message)


# 0-3 Например:
# thing = input('Скажи что нибудь: ')
# print('Ты сказал слова \n... {}'.format(thing))


# 1. Пример
# start_war = 1941
# end_war = 1945
# war_text = 'Экинчи дуйнолук согуш {}-жылы башталып, {}-жылы аяктаган'.format(start_war, end_war)
# print(war_text)


# 2 Пример
# cats = ['сулоосун', 'жолборс', 'арстан']
# message = '{2}, {1}, {0} мышык сымал жаныбарлардын катарына кирет.'.format(cats[0], cats[1], cats[2])
# print(message)

#3 Пример:
# asia = ['Kyrgyzstan', 'Afganistan', 'Uzbekistan']
# msg = 'Орто Азиядагы мамлекеттер: \n{} \n{} \n{}'.format(asia[0], asia[1], asia[2])
# print(msg)

#4 Пример:
# a = 'ФЕЙК'
# lorem = '''Lorem Ipsum is simply dummy text {0} of the printing {0} and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled {0} it to make a type specimen book. It has survived not only five centuries, but also {0} the leap into electronic typesetting, remaining essentially unchanged. It was {0} popularised in the 1960s with the release of Letraset sheets {0} containing {0} Lorem Ipsum passages, and more recently with desktop publishing software {0} like Aldus PageMaker including versions of Lorem Ipsum.
# '''.format(a)
# print(lorem)