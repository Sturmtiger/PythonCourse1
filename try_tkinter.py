# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()





# from tkinter import *
# root = Tk()
# root.title("Hello World!")
# root.geometry('400x200')
# def button_clicked():
#     print("Hello World!")
# def close():
#     root.destroy()
#     root.quit()
# button = Button(root, text="Press Me", command=button_clicked)
# button.pack(fill=BOTH)
# root.mainloop()





# from tkinter import *
# root = Tk()
#
# top_frame = Frame(root)
# top_frame.pack()
#
# bottom_frame = Frame(root)
# bottom_frame.pack(side=BOTTOM)
#
# left_frame = Frame(root)
# left_frame.pack(side=LEFT)
#
# right_frame = Frame(root)
# right_frame.pack(side=RIGHT)
#
# button1 = Button(top_frame, text='Первая', fg='black', bg='purple')
# button2 = Button(left_frame, text='Вторая', fg='red', font=("symbol", 10, "bold"))
# button3 = Button(right_frame, text='Третья', fg='pink')
# button4 = Button(bottom_frame, text='Четвертая', fg='purple')
#
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()
#
# root.mainloop()




# from tkinter import *
# import time
# def button_clicked():
#     # изменяем текст кнопки
#     button['text'] = time.strftime('%H:%M:%S')
# root=Tk()
# # создаём виджет
# button = Button(root)
# # конфигурируем виджет после создания
# button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
# # также можно использовать квадратные скобки:
# # button['text'] = time.strftime('%H:%M:%S')
# # button['command'] = button_clicked
# button.pack()
# root.mainloop()




# from tkinter import *
# from random import random
# def button_clicked():
#     button['text'] = button['bg'] # показываем предыдущий цвет кнопки
#     bg = '#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16))
#     print(bg)
#     button['bg'] = bg # bg - цвет кнопки
#     button['activebackground'] = bg # activebackground - цвет кнопки при нажатии
# root=Tk()
# button = Button(root, command=button_clicked)
# button.pack()
# root.mainloop()


# from tkinter import *
# def hide_show():
#     if label.winfo_viewable():
#         label.grid_remove()
#     else:
#         label.grid()
# root=Tk()
# label = Label(text='Я здесь!')
# label.grid()
# button = Button(command=hide_show, text="Спрятать/Открыть")
# button.grid()
# root.mainloop()

# from tkinter import *
# root=Tk()
# root.after(200, root.grab_set_global)
# root.after(1000, root.grab_release)
# root.mainloop()


import tkinter as tk


class App:
    """"""

    def __init__(self, parent):
        """Конструктор"""
        frame = tk.Frame(parent)
        frame.pack()

        btn22 = tk.Button(
            frame,
            text="22",
            command=lambda: self.printNum(22)
        )
        btn22.pack(side=tk.LEFT)

        btn44 = tk.Button(
            frame,
            text="44",
            command=lambda: self.printNum(44)
        )
        btn44.pack(side=tk.LEFT)

        quitBtn = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
        quitBtn.pack(side=tk.LEFT)

    def printNum(self, num):
        print("Вы нажали кнопку: %s" % num)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()