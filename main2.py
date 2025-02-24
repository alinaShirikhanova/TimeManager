from tkinter import *

is_running = False  # Флаг, запущен ли таймер
timer_id = None
def toggle_timer():
    global is_running, timer_id
    if is_running:
        is_running = False
        if timer_id is not None:
            root.after_cancel(timer_id)
            timer_id = None
        start_button.config(text="Старт")
    else:
        is_running = True
        start_button.config(text="Пауза")

# Создаем главное окно приложения
root = Tk()
root.geometry('500x500')  # Устанавливаем размер окна
root.title('Time manager')  # Заголовок окна

# Определяем шрифт, который будем использовать в интерфейсе
font_style = 'Arial'

# Создаем основной фрейм для размещения кнопок и таймера
main_frame = Frame(master=root)

# Кнопка для начала работы (переключает режим в "работу")
work_button = Button(master=main_frame, text='Работа', width=10, font=(font_style, 14))
work_button.grid(row=0, column=0, padx=10, pady=10)  # Размещаем кнопку в сетке (первая строка, первый столбец)

# Кнопка для начала перерыва (переключает режим в "перерыв")
break_button = Button(master=main_frame, text='Перерыв', width=10, font=(font_style, 14))
break_button.grid(row=0, column=1, padx=10, pady=10)  # Размещаем кнопку в сетке (первая строка, второй столбец)

# Размещаем фрейм в главном окне с отступом сверху
main_frame.pack(pady=20)

# Метка для отображения таймера (по умолчанию 25 минут)
time_label = Label(master=main_frame, text='25:00', font=(font_style, 60))
time_label.grid(row=1, column=0, columnspan=2)  # Размещаем метку во второй строке, растягиваем на два столбца

# Кнопка "Старт" для запуска таймера
start_button = Button(master=main_frame, text='start', width=10, font=(font_style, 20), command=toggle_timer)
start_button.grid(row=2, column=0, columnspan=2)  # Размещаем кнопку в третьей строке, растягиваем на два столбца

# Дополнительные кнопки
sound_button = Button(main_frame, text="Звук", font=(font_style, 14), width=10)
sound_button.grid(row=3, column=0, pady=10, padx=10)

task_button = Button(main_frame, text="Банк заданий", font=(font_style, 14), width=10)
task_button.grid(row=3, column=1, pady=10, padx=10)
# Запускаем главный цикл обработки событий
root.mainloop()














# # import tkinter
# # from tkinter import Tk, и тд
# from tkinter import *
# root = Tk()
#
#
#
#
#
#
# root.mainloop()






# from tkinter import *
#
# root = Tk()
# root.geometry('500x500')
# root.title('Time manager')
# font_style = 'Arial'
#
# main_frame = Frame(master=root)
# work_button = Button(master=main_frame, text='Работа', width=10, font=(font_style, 14))
# work_button.grid(row=0, column=0, padx=10, pady=10)
#
# break_button = Button(master=main_frame, text='Перерыв', width=10, font=(font_style, 14))
# break_button.grid(row=0, column=1, padx=10, pady=10)
# main_frame.pack(pady=20)
#
# time_label = Label(master=main_frame, text='25:00', font=(font_style, 60))
# time_label.grid(row=1, column=0, columnspan=2)
#
# start_button = Button(master=main_frame, text='start', width=10, font=(font_style, 20))
# start_button.grid(row=2, column=0, columnspan=2)
# root.mainloop()






