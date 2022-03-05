#!/usr/bin/python
# -*- coding: utf-8 -*-
# На прошлом уроке у нас добавился модуль Label, он служит нам для написания текста на нашем графическом интерфейсе. Но мы видим, что у нас добавился еще один модуль - Menu. Как раз чем мы на этом уроке и занимались - созданием меню.
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

    # Кнопки в нашем меню пункта "Параметры" должны ссылаться на какие-то подпрограммы, чтобы их выполнять, а так как мы делаем сейчас только "косметическую" часть, то эти подпрограммы у нас просто "пустышки".
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

    # Тоже самое делаем для нашего пункта меню "Фильтры".
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

    def rnd_green_click(self):
        pass

    def rnd_blue_click(self):
        pass

    def rnd_biruza_click(self):
        pass

    def rnd_fiol_click(self):
        pass

    def rnd_lilov_click(self):
        pass

    def random_color_click(self):
        pass

    def create_menu(self):
        # Обозначаем в программе, что у нас будет создано меню.
        menu = Menu(self.parent)
        # Присваиваем нашему меню три вкладки - file_menu, filters_menu, parametr_menu.
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

        # Теперь мы наши созданные вкладки "обзываем", присваивая каждой свое название.
        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)
        # Здесь мы уже с помощью функции add_command() - создаем подкатегории (пункты каждой вкладки). Как мы и говорили раньше - все кнопки, кроме "Открыть" и "Выход" у нас изначально имеют статус "Неактивно", здесь тоже нет никаких исключений. С помощью функции - add_separator(), мы добавляем разделяющую горизонтальную линию. А с помощью команды - command=self.open, мы даем понять, что при нажатии на кнопку меню "Открыть" - должна сработать подпрограмма open().
        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save, state='disabled')
        self.file_menu.add_command(label="Очистить", command=self.clear, state='disabled')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)
        # Тоже самое проделываем со второй вкладкой "Параметры" и "Фильтры", мы обращаемся с начала к ней - self.parametr_menu (пункт "Параметры") и self.filters_menu (пункт "Фильтры"), потом применяем функцию - add_command(), которая нам и позволяет добавить пункты во вкладку.
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
        self.filters_menu.add_command(label="Оттенки зеленого ",
                                      command=self.rnd_green_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки синего",
                                      command=self.rnd_blue_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки бирюзового ",
                                      command=self.rnd_biruza_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки фиолетового ",
                                      command=self.rnd_fiol_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки лилового ",
                                      command=self.rnd_lilov_click, state='disabled')
        self.filters_menu.add_command(label="Случайные цвета",
                                      command=self.random_color_click, state='disabled')

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
        # Добавляем функционал, а точнее передаем нашему окну параметр того, что у нас будет создано меню.
        self.parent.config(menu=menu)


if __name__ == '__main__':
    root = Tk()
    root.title("Урок 2 - Создание вкладок дополнительного меню")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
