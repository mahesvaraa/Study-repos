#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar, Label, Menu

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

    def save(self):
        pass

    def clear(self):
        pass

    def close(self):
        pass

    def brightness_click(self):
        pass

    def contrast_click(self):
        pass

    def rgb_balans_click(self):
        pass

    def choice_big(self):
        pass

    def choice_small(self):
        pass

    def choice_rotation(self):
        pass

    def negativ_clic(self):
        pass

    def rnd_noise_click(self):
        pass

    def gray_click(self):
        pass

    def sepia_click(self):
        pass

    def black_white_click(self):
        pass

    def rnd_red_click(self):
        pass

    def create_menu(self):
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)

        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save, state='disabled')
        self.file_menu.add_command(label="Очистить", command=self.clear, state='disabled')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)

        self.parametr_menu.add_command(label="Яркость", command=self.brightness_click,
                                       state='disabled')
        self.parametr_menu.add_command(label="Контрастность",
                                       command=self.contrast_click, state='disabled')
        self.parametr_menu.add_command(label="Цветовой баланс",
                                       command=self.rgb_balans_click, state='disabled')
        self.parametr_menu.add_command(label="Увеличить", command=self.choice_big,
                                       state='disabled')
        self.parametr_menu.add_command(label="Уменьшить", command=self.choice_small,
                                       state='disabled')
        self.parametr_menu.add_command(label="Повернуть", command=self.choice_rotation,
                                       state='disabled')

        self.filters_menu.add_command(label="Негатив", command=self.negativ_clic,
                                      state='disabled')
        self.filters_menu.add_command(label="Шум", command=self.rnd_noise_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Оттенки серого", command=self.gray_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Сепия", command=self.sepia_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Черно-белый",
                                      command=self.black_white_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки красного",
                                      command=self.rnd_red_click, state='disabled')

        label_fail = Label(root, text='Параметры файла')
        label_fail.place(x=22, y=30)

        self.btn_open = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btn_open.place(x=25, y=60)

        self.btn_save = Button(text="Сохранить", height=2, width=12, command=self.save,
                               state='disabled')
        self.btn_save.place(x=25, y=105)

        self.btn_clear = Button(text="Очистить", height=2, width=12, command=self.clear,
                                state='disabled')
        self.btn_clear.place(x=25, y=150)

        self.btn_exit = Button(text="Выход", height=2, width=12, command=self.close)
        self.btn_exit.place(x=25, y=195)
        # Используем функцию Label для того, чтобы на нашем интерфейсе расположить надпись, указываем ей название и расположение по координатам относительно левого верхнего угла.
        label_fail_par = Label(root, text='Параметры изображения')
        label_fail_par.place(x=650, y=30)
        # Далее создаем нашу первую кнопку из блока "Параметры изображения" - "Яркость", так как мы во втором уроке создавали подпрограммы (пустышки) для нашего меню "Параметры", а там точно такие же кнопки, то просто указываем для кнопок к каким функциям им нужно обращаться - command=self.brightness_click, указываем размер и положение нашей кнопки.
        self.btn_yar = Button(text="Яркость", height=2, width=12,
                              command=self.brightness_click, state='disabled')
        self.btn_yar.place(x=675, y=60)
        # Тоже самое делаем для кнопок "Контрастность" и "RGB баланс".
        self.btn_contr = Button(text="Контрастность", height=2, width=12,
                                command=self.contrast_click, state='disabled')
        self.btn_contr.place(x=675, y=105)

        self.btn_cvb = Button(text="RGB баланс", height=2, width=12,
                              command=self.rgb_balans_click, state='disabled')
        self.btn_cvb.place(x=675, y=150)

        self.btn_cvb = Button(text="Увеличить", height=2, width=12,
                              command=self.choice_big, state='disabled')
        self.btn_cvb.place(x=675, y=200)

        self.btn_cvb = Button(text="Уменьшить", height=2, width=12,
                              command=self.choice_small, state='disabled')
        self.btn_cvb.place(x=675, y=250)

        self.btn_cvb = Button(text="Повернуть", height=2, width=12,
                              command=self.choice_rotation, state='disabled')
        self.btn_cvb.place(x=675, y=300)

        self.parent.config(menu=menu)


if __name__ == '__main__':
    root = Tk()
    root.title("Урок 3 - Создание блока 'Параметры изображения'")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
