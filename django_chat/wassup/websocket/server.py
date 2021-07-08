import websockets
import asyncio
import json

# здесь храним подключенных к серверу клиентов
users = set()


async def message(websocket, path):
    while True:
        # получаем сообщение из клиента в формате JSON
        json_response = await websocket.recv()

        # преобразуем json ответ в dict
        response_dict = json.loads(json_response)

        # Выводим сообщение клиента для дебагга
        print('Сообщение', response_dict['message'])

        # Проверяем если клиент впервые подключается
        if response_dict['message'] == 'init':
            # когда пользователь первые подключается
            # мы его запоминаем в переменную users
            users.add(websocket)
            for user in users:
                response_dict['message'] = 'вошел'

                if user.closed == False:
                    # отправляем клиенту JSON
                    await user.send(json.dumps(response_dict))
        else:
            # отправляем сообщение всем
            for user in users:
                if user.closed == False:
                    await user.send(json_response)


# Создаем сервер веб чата на порту 3030
server = websockets.serve(message, port=3030)
print('Наш веб чат сервер запущен...')

# Запуск веб чат сервера
asyncio.get_event_loop().run_until_complete(server)
# Запуск сервера на постоянную основу
asyncio.get_event_loop().run_forever()
