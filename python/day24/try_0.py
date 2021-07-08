task_file = open('tasks.txt', 'r')
task_lists = task_file.readlines()


for task in task_lists:
    try:
        t = task.strip()
        print(t, '=', eval(t))
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except FileNotFoundError:
        print('Файл не найден')
    except:
        print('Выражение неправилен')