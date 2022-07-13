#!/usr/bin/python
# -*- coding: utf-8 -*-
# В этом примере мы расположили три изображения при помощи абсолютного позиционирования. Мы использовали менеджер геометрии place.

from tkinter import Tk, Label, BOTH, Frame

# Мы использовали Image и ImageTk из модуля PIL (Python Imaging Library).
from PIL import Image, ImageTk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()

    def create_menu(self):
        self.pack(fill=BOTH, expand=1)
        # Мы создали объект изображения и объект фото изображения из изображения в текущей рабочей директории.
        tiger = Image.open("1.jpg")
        tigrula = ImageTk.PhotoImage(tiger)
        # Мы создали Label (ярлык) с изображением. Данные ярлыки могут содержать как изображения, так и текст.
        label1 = Label(self, image=tigrula)
        # Нам нужно сохранять ссылку на изображение, чтобы не потерять его среди разного "мусора".
        label1.image = tigrula
        # Ярлык размещен в рамке по координатам x=50 и y=40.
        label1.place(x=50, y=40)

        medved = Image.open("1.jpg")
        vinipuh = ImageTk.PhotoImage(medved)
        label2 = Label(self, image=vinipuh)
        label2.image = vinipuh
        label2.place(x=50, y=300)

        telefon = Image.open("1.jpg")
        tel = ImageTk.PhotoImage(telefon)
        label3 = Label(self, image=tel)
        label3.image = tel
        label3.place(x=450, y=40)

        cat = Image.open("1.jpg")
        cat1 = ImageTk.PhotoImage(cat)
        label3 = Label(self, image=cat1)
        label3.image = cat1
        label3.place(x=450, y=300)


if __name__ == '__main__':
    root = Tk()
    root.title("Пример 3 - Абсолютное позиционирование в Tkinter")
    root.geometry("800x500+250+100")
    app = Example(root)
    root.mainloop()
