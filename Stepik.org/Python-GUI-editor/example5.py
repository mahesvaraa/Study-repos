#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Подключили дополнительные библиотеки для открытия изображений, диалогового окна и скроллбаров.
from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar

from PIL import ImageTk, Image


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()
        # Обозначаем, что изначально у нас нету никаких изображений
        self.image = None
        self.photo = None
        # Создаем на нашем интерфейсе область, в которую будем загружать наши изображения. Зададим ей изначальный фон
        # - серый, размер 400х400 и укажем, что при загрузке изображений они располагались по координатам (0,0).
        self.display = Canvas(self.parent, bg="gray")
        self.display_img = self.display.create_image(0, 0)
        self.display.pack()

    def open(self):
        #  Открытие диалогового окна для выбора изображения.
        self.filename = filedialog.askopenfilename()
        # Открываем выбранное нами изображение, загружаем его на созданный нами дисплей (полотно) display_img().
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        # Устанавливаем вертикальный и горизонтальный скроллбарр по координатам (x,y) для того, чтобы большие
        # изображения мы смогли просматривать полностью.
        self.scr1 = Scrollbar(root, command=self.display.yview, orient='vertical')
        self.scr1.place(x=133, y=3)

        self.scr2 = Scrollbar(root, command=self.display.xview, orient="horizontal")
        self.scr2.place(x=145, y=452)

    # Создаем кнопку "Открыть". По нажатию на эту кнопку, будет срабатывать подпрограмма open(self),
    # которая открывает диалоговое окно для выбора изображения и загружает его в нами выбранную область.
    def create_menu(self):
        self.btn_open = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btn_open.place(x=25, y=60)


if __name__ == '__main__':
    root = Tk()
    root.title("Пример 1 - Использование Pillow. Загрузка изображения")
    root.geometry("700x500+250+100")
    app = Example(root)
    root.mainloop()
