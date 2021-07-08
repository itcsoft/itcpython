
def request_time(func):
    import time
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения', end - start, 'секунд.')
    return inner


@request_time
def get_web_site():
    import requests
    webpage = requests.get('https://super.kg')
    print('Запрос завершен')


@request_time
def factorial():
    number = 100_000
    current = 1
    fact = 1
    while current <= number:
        fact = fact * current
        current = current + 1
    print(fact)


factorial()