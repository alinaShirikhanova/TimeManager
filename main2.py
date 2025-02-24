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






from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Time manager')
font_style = 'Arial'

main_frame = Frame(master=root)
work_button = Button(master=main_frame, text='Работа', width=10, font=(font_style, 14))
work_button.grid(row=0, column=0, padx=10, pady=10)

break_button = Button(master=main_frame, text='Перерыв', width=10, font=(font_style, 14))
break_button.grid(row=0, column=1, padx=10, pady=10)
main_frame.pack(pady=20)

time_label = Label(master=main_frame, text='25:00', font=(font_style, 60))
time_label.grid(row=1, column=0, columnspan=2)

start_button = Button(master=main_frame, text='start', width=10, font=(font_style, 20))
start_button.grid(row=2, column=0, columnspan=2)
root.mainloop()






