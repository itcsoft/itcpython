from tkinter import Tk, Menu
from db import sqlite
import function as fn

app_title = 'first app'
app_size = '300x200'

# заготовка для запроса
dbcursor = sqlite.cursor()
dbcursor.execute('SELECT * FROM settings')

# получаем настройки из базы данных
settings = dbcursor.fetchall()

# начальные настройки для приложения
for config in settings:
    print(config)
    if config[1] == 'title':
        app_title = config[2]
    if config[1] == 'size':
        app_size = config[2]

# Главная программа
mainApp = Tk()
mainApp.title(app_title)

# размер окна width 600px height 300px
mainApp.geometry(app_size)

# flabel = Label(mainApp, text = 'Hello world', font = ('Calibri', 24))
# flabel.grid(column = 30, row = 20)

# Создание главного меню
mainMenus = Menu(mainApp)

fileMenu = Menu(mainMenus, tearoff=0)
fileMenu.add_command(label = 'Настройки')
fileMenu.add_separator()
fileMenu.add_command(label = 'Закрыть', command = fn.exit_program)

productMenu = Menu(mainMenus, tearoff=0)
productMenu.add_command(
    label = 'Добавить',
    command = fn.create_product_window
)
productMenu.add_command(label = 'Список')

mainMenus.add_cascade(label = 'Файл', menu = fileMenu)
mainMenus.add_cascade(label = 'Продукты', menu = productMenu)
mainMenus.add_command(label = 'Справка')

# инициализация меню
mainApp.config( menu = mainMenus )
mainApp.mainloop()