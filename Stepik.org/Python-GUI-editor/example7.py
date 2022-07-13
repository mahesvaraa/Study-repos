#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar

from PIL import ImageTk, Image


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()

        self.image = None
        self.photo = None

        self.display = Canvas(self.parent, width=400, height=400, bg="gray")
        self.display_img = self.display.create_image(0, 0)
        self.display.pack()

    def open(self):
        self.filename = filedialog.askopenfilename()

        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

        self.scr1 = Scrollbar(root, command=self.display.yview, orient='vertical')
        self.scr1.place(x=133, y=3)

        self.scr2 = Scrollbar(root, command=self.display.xview, orient="horizontal")
        self.scr2.place(x=145, y=452)

    # Ну и конечно же, не забудем о том, что нам нужно создать кнопку, а то без нее и ничего у нас не получиться.
    # Создаем кнопку, задаем ей размеры, положение и "говорим" нашей кнопке, чтобы по нажатию она обращалась к
    # подпрограмме miniatura(), о которой мы говорили выше.
    def miniatura(self):
        image = Image.open(self.filename)

        image = image.resize((150, 150), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

    def create_menu(self):
        self.btn_open = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btn_open.place(x=25, y=60)
        # Ну и конечно же, не забудем о том, что нам нужно создать кнопку, а то без нее и ничего у нас не получиться.
        # Создаем кнопку, задаем ей размеры, положение и "говорим" нашей кнопке, чтобы по нажатию она обращалась к
        # подпрограмме miniatura(), о которой мы говорили выше.
        self.btn_mini = Button(text="Миниатюра", height=2, width=12, command=self.miniatura)
        self.btn_mini.place(x=25, y=120)


if __name__ == '__main__':
    root = Tk()
    root.title("Пример 3 - Создание миниатюры изображения")
    root.geometry("700x500+250+100")
    app = Example(root)
    root.mainloop()
