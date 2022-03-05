#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, BOTH, X, N, LEFT, Frame, Label, Entry


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()

    # Первая рамка является базовой. На ней располагаются все остальные рамки.
    # Стоит отметить, что даже при организации дочерних виджетов в рамках, мы управляем ними на базовой рамке.
    def create_menu(self):
        self.pack(fill=BOTH, expand=True)
        # Первые два виджета размещены на первой рамке.
        # Поле для ввода растянуто горизонтально с параметрами fill и expand.
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Заголовок", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Автор", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        # В третьей рамке мы разместили ярлык и виджет текста.
        # Ярлык закреплен по северной стороне, а виджет текста занимает все остальное пространство.
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Сообщение", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


if __name__ == '__main__':
    root = Tk()
    root.title("Пример 4 - Обзор разметки для создания GUI в Tkinter")
    root.geometry("500x350+250+100")
    app = Example(root)
    root.mainloop()
