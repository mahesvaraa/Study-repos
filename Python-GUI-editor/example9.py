# Для того, чтобы у нас появилось название нашего блока, чтобы мы смогли использовать label, то нам для начала нужно подключить соответствующий модуль Label из нашей библиотеки thinker. Что мы собственно и делаем.
from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar, Label

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

    # Создаем "пустышку" нашей подпрограммы сохранения изображения. Заполнять ее функцией мы будем в другом разделе урока, пока что нам нужно создать макет.
    def save(self):
        pass

    def create_menu(self):
        # Используем функцию Label для того, чтобы на нашем интерфейсе расположить надпись, указываем ей название и расположение по координатам относительно левого верхнего угла.
        label_fail = Label(root, text='Параметры файла')
        label_fail.place(x=22, y=30)

        self.btn_open = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btn_open.place(x=25,
                            y=60)  # Далее создаем нашу вторую кнопку "Сохранить", подключаем к ней нашу подпрограмму (пустышку), указываем размер и положение нашей кнопки. Все кнопки, кроме кнопки "Открыть" и "Выход" будут изначально у нас со статусом "Неактивно" - state='disabled',  это будет сделано для того, чтобы пользователь сначала открыл картинку, а только потом производил над ней манипуляции, а то просто "тыкать" кнопки по пустой области, как-то не очень!
        self.btn_save = Button(text="Сохранить", height=2, width=12, command=self.save,
                               state='disabled')
        self.btn_save.place(x=25, y=105)


if __name__ == '__main__':
    root = Tk()
    root.title("Урок 1 - Создание блока кнопок 'Параметры файла'")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
