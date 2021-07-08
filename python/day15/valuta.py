# Курс валют
curs = {
    "EUR": 101.65,
    "USD": 84.80,
    "RUS": 1.23,
    "KZT": 0.200
}

# Мен сом турундо акчаны берсем валюта боюнча
# конвертация кылып бер.
# Мисалы: 60 000 сомду доллар кылып бер
# 78 685 сомду Евро кылып бер
# 50 000 сомду Тенге кылып бер
# 45 000 сомду Рубль кылып бер

def convert(money, valuta):
    if curs.get(valuta) != None:
        result = money / curs[valuta]
        print(valuta, ':', result)
    else:
        print('Андай валюта жок')
    

valuta = input('Кайсы валютага которосуз: ')
money = float(
    input('Сумманы айтыныз сом турундо: ')
)

convert(money, valuta)