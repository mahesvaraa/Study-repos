#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, BOTH, Button, messagebox


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.create_menu()

    def close(self):
        if messagebox.askyesno('Выход', 'Вы уверены?'):
            self.parent.destroy()

    def create_menu(self):
        self.pack(fill=BOTH, expand=1)
        self.btn_exit = Button(text="Выход", height=2, width=12, command=self.close)
        self.btn_exit.place(x=25, y=195)


if __name__ == '__main__':
    root = Tk()
    root.title("Пример 2 - Кнопка выхода со всплывающим модальным окном подтверждения")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
