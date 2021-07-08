# Задание 4:
# Спрсите у пользователя строку НА Английском или целое предложение и удалите все глассные буквы там.
# То что осталось от строки выведите на экран.
# Строка не должна быть короче 10 символов.

unduulor = ['a', 'u', 'i','e','y','o']
word = input('Введите текст на английском: ')

word_exclude = ''
for w in list(word):
    if not unduulor.count(w.lower()):
        word_exclude = word_exclude + w

print(word_exclude)