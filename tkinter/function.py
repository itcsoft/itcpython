from tkinter import Toplevel, Label, Entry, Button


# функция для закрытия программы
def exit_program():
    exit()


# создаем форму добавления продукта
def create_product_window():
    product_add_window = Toplevel()
    product_add_window.wm_title(
        'Форма добавления продукта'
    )
    product_add_window.geometry('500x350')

    lbl_name = Label(product_add_window, text = 'Название:')
    lbl_name.grid(column = 1, row = 0)
    inp = Entry(product_add_window, width = 20)
    inp.grid(column = 2, row = 0)
    btn = Button(product_add_window, text = 'добавить')
    btn.grid(column = 3, row = 0)


