#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Frame, Menu, Label, Canvas, Button, Tk, Scale
from tkinter import Scrollbar, filedialog, messagebox, CENTER

from PIL import ImageTk, Image, ImageDraw


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()

        self.image = None
        self.photo = None

    def open(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.image = Image.open(self.filename)
            print(self.image.height, self.image.width, )
            self.image = self.image.resize(
                (int(self.image.width * (400 / self.image.width)), int(self.image.height * (400 / self.image.width))),
                Image.ANTIALIAS)  # <----

            self.photo = ImageTk.PhotoImage(self.image)
            self.display = Canvas(self.parent, width=self.photo.width(), height=self.photo.height())
            self.display_img = self.display.create_image(0, 0)
            self.display.pack()
            self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

            self.file_menu.entryconfig("Сохранить", state='active')
            self.file_menu.entryconfig("Очистить", state='active')

            self.parametr_menu.entryconfig("Яркость", state='active')
            self.parametr_menu.entryconfig("Контрастность", state='active')
            self.parametr_menu.entryconfig("Цветовой баланс", state='active')

            self.scr1 = Scrollbar(root, command=self.display.yview, orient='vertical')
            self.scr1.place(x=133, y=3)

            self.scr2 = Scrollbar(root, command=self.display.xview, orient="horizontal")
            self.scr2.place(x=145, y=452)

            self.btn_save.config(state="normal")

            self.btn_yar.config(state="normal")
            self.btn_contr.config(state="normal")
            self.btn_cvb.config(state="normal")
            self.orig = self.photo

    def save(self):
        path = filedialog.asksaveasfilename()
        if path:
            try:
                self.image.save(path)
                messagebox.showinfo('Сохранение', 'Успех! Файл сохранен.')
            except KeyError:
                messagebox.showerror('Ошибка', 'Не задано расширение')

    def brightness(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        factor = self.scale.get()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + factor
                b = pix[i, j][1] + factor
                c = pix[i, j][2] + factor
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def brightness_click(self):
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (200, 200, 400, 400))
        label = Label(root, text='Выберете значение яркости')
        label.pack(anchor=CENTER)

        self.scale = Scale(root, from_=-100, to=100, orient="horizontal")
        self.scale.pack(anchor=CENTER)

        def reset_brightness():
            self.brightness()

        def close():
            root.destroy()

        button_rnd = Button(root, text="Ок", command=reset_brightness)
        button_rnd.place(x=25, y=70)

        button_close = Button(root, text="Закрыть", command=close)
        button_close.place(x=70, y=70)

    def contrast(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        factor = self.scale_contrast.get()
        contrast1 = (259 * (factor + 255)) / (255 * (259 - factor))
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                a = round(contrast1 * (a - 128) + 128)
                b = round(contrast1 * (b - 128) + 128)
                c = round(contrast1 * (c - 128) + 128)
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def contrast_click(self):
        root_contrast = Tk()
        root_contrast.geometry('%dx%d+%d+%d' % (150, 100, 400, 400))
        label_contrast = Label(root_contrast, text='Выберете значение контрастности')
        label_contrast.pack(anchor=CENTER)
        self.scale_contrast = Scale(root_contrast, from_=-100, to=100, orient="horizontal")
        self.scale_contrast.pack(anchor=CENTER)

        def reset_contrast():
            self.contrast()

        def close():
            root_contrast.destroy()

        button_rnd = Button(root_contrast, text="Ок", command=reset_contrast)
        button_rnd.place(x=25, y=62)
        button_close = Button(root_contrast, text="Закрыть", command=close)
        button_close.place(x=70, y=62)

    def rgb_balans(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + self.scale_r.get()
                b = pix[i, j][1] + self.scale_g.get()
                c = pix[i, j][2] + self.scale_b.get()
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def rgb_balans_click(self):
        root_rgb_balans = Tk()
        root_rgb_balans.geometry('%dx%d+%d+%d' % (200, 225, 400, 400))

        label_r = Label(root_rgb_balans, text='Выберите значение краcного')
        label_r.pack(anchor=CENTER)
        self.scale_r = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_r.pack(anchor=CENTER)

        label_g = Label(root_rgb_balans, text='Выберите значение зеленого')
        label_g.pack(anchor=CENTER)
        self.scale_g = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_g.pack(anchor=CENTER)

        label_b = Label(root_rgb_balans, text='Выберите значение синего')
        label_b.pack(anchor=CENTER)
        self.scale_b = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_b.pack(anchor=CENTER)

        def reset_rgb_balans():
            self.rgb_balans()

        def close():
            root_rgb_balans.destroy()

        button_rnd = Button(root_rgb_balans, text="Ок", command=reset_rgb_balans)
        button_rnd.place(x=45, y=190)
        button_close = Button(root_rgb_balans, text="Закрыть", command=close)
        button_close.place(x=100, y=190)

    def clear(self):
        self.display.itemconfigure(self.display_img, image=self.orig, anchor="nw")

    def close(self):
        if messagebox.askyesno('Выход', 'Вы уверены?'):
            self.parent.destroy()
        elif messagebox.showinfo('Выход', "Выход отменен"):
            pass

    def choice_big(self):
        draw = ImageDraw.Draw(self.image)
        self.image.size = (self.image.size[0] * 2, self.image.size[1] * 2)

        pix = self.image.load()
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

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
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)

        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save)
        self.file_menu.add_command(label="Очистить", command=self.clear)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)

        self.parametr_menu.add_command(label="Яркость", command=self.brightness_click,
                                       state='disabled')
        self.parametr_menu.add_command(label="Контрастность",
                                       command=self.contrast_click, state='disabled')
        self.parametr_menu.add_command(label="Цветовой баланс",
                                       command=self.rgb_balans_click, state='disabled')
        self.parametr_menu.add_command(label="Увеличить", command=self.choice_big)
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

        self.btn_save = Button(text="Сохранить", height=2, width=12, command=self.save)
        self.btn_save.place(x=25, y=105)

        self.btn_clear = Button(text="Очистить", height=2, width=12, command=self.clear)
        self.btn_clear.place(x=25, y=150)

        self.btn_exit = Button(text="Выход", height=2, width=12, command=self.close)
        self.btn_exit.place(x=25, y=195)

        label_fail_par = Label(root, text='Параметры изображения')
        label_fail_par.place(x=650, y=30)

        self.btn_yar = Button(text="Яркость", height=2, width=12,
                              command=self.brightness_click, state='disabled')
        self.btn_yar.place(x=675, y=60)

        self.btn_contr = Button(text="Контрастность", height=2, width=12,
                                command=self.contrast_click, state='disabled')
        self.btn_contr.place(x=675, y=105)

        self.btn_cvb = Button(text="RGB баланс", height=2, width=12,
                              command=self.rgb_balans_click, state='disabled')
        self.btn_cvb.place(x=675, y=150)

        self.btn_big = Button(text="Увеличить", height=2, width=12,
                              command=self.choice_big, state='disabled')
        self.btn_big.place(x=675, y=195)

        self.btn_small = Button(text="Уменьшить", height=2, width=12,
                                command=self.choice_small, state='disabled')
        self.btn_small.place(x=675, y=240)

        self.btn_rotate = Button(text="Повернуть", height=2, width=12,
                                 command=self.choice_rotation, state='disabled')
        self.btn_rotate.place(x=675, y=285)

        self.parent.config(menu=menu)


if __name__ == '__main__':
    root = Tk()
    root.title("Урок 4 - Добавления функционала кнопок 'Параметры файла'")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
