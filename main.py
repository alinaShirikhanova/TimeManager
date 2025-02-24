import tkinter as tk
from tkinter import messagebox

# Основное окно
root = tk.Tk()
root.title("Time manager")

# Переменные для времени
work_time = 25 * 60  # 25 минут работы
break_time = 5 * 60  # 5 минут перерыва
current_time = work_time
is_working = True
is_running = False  # Флаг, запущен ли таймер
timer_id = None     # Идентификатор для отмены scheduled вызова

def update_label():
    minutes, seconds = divmod(current_time, 60)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

def update_timer():
    global current_time, timer_id
    if is_running:
        update_label()
        if current_time > 0:
            current_time -= 1
            timer_id = root.after(1000, update_timer)
        else:
            switch_mode()

def switch_mode():
    global current_time, is_working, timer_id, is_running
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    is_running = False
    if is_working:
        current_time = break_time
        is_working = False
        messagebox.showinfo("Перерыв", "Время на перерыв! Расслабься!")
    else:
        current_time = work_time
        is_working = True
        messagebox.showinfo("Работа", "Время вернуться к работе!")
    update_label()
    update_start_button()

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
        update_timer()
        start_button.config(text="Пауза")

def start_work():
    global current_time, is_working, timer_id, is_running
    # При переключении отменяем запланированный отсчёт и ставим таймер на паузу
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    is_running = False
    is_working = True
    current_time = work_time
    update_label()
    update_start_button()

def start_break():
    global current_time, is_working, timer_id, is_running
    # При переключении отменяем запланированный отсчёт и ставим таймер на паузу
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    is_running = False
    is_working = False
    current_time = break_time
    update_label()
    update_start_button()

def show_task_bank():
    task_window = tk.Toplevel(root)
    task_window.title("Банк заданий")

    tasks = ["Задание 1", "Задание 2", "Задание 3", "Задание 4", "Задание 5"]
    task_listbox = tk.Listbox(task_window)
    for task in tasks:
        task_listbox.insert(tk.END, task)
    task_listbox.pack()

def update_start_button():
    if is_running:
        start_button.config(text="Пауза")
    else:
        start_button.config(text="Старт")

# Размещение элементов в окне
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Кнопки переключения режимов
work_button = tk.Button(frame, text="Работа", font=("Arial", 14), width=10, command=start_work)
work_button.grid(row=0, column=0, padx=10, pady=10)

break_button = tk.Button(frame, text="Перерыв", font=("Arial", 14), width=10, command=start_break)
break_button.grid(row=0, column=1, padx=10, pady=10)

# Таймер в центре
timer_label = tk.Label(frame, text="25:00", font=("Arial", 30), width=10)
timer_label.grid(row=1, column=0, columnspan=2, pady=20)

# Кнопка старт/пауза
start_button = tk.Button(frame, text="Старт", command=toggle_timer, font=("Arial", 14), width=15)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

# Дополнительные кнопки
sound_button = tk.Button(frame, text="Звук", font=("Arial", 14), width=10)
sound_button.grid(row=3, column=0, pady=10)

task_button = tk.Button(frame, text="Банк заданий", command=show_task_bank, font=("Arial", 14), width=10)
task_button.grid(row=3, column=1, pady=10)

root.mainloop()
