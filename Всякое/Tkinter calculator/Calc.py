import re
from math import *
from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.formula = ''
        self.lbl = ''
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#FFF", foreground="#000")
        self.lbl.place(x=11, y=50)
        x, y = 10, 140
        btns = [
            "π", "e", "C", "⇐",
            "x²", '√', "lg", 'ln',
            "(", ")", "n!", "*",
            "7", "8", "9", "/",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "±", "0", ".", "=",
        ]

        for bt in btns:
            Button(text=bt, font=("Century Gothic", 20), bg="#FFF",
                   command=lambda x=bt: self.logicalc(x)).place(x=x, y=y, width=80, height=50)
            x += 81
            if x > 300:
                x = 10
                y += 52

        root.bind("<Key>", self.print_key)

    def print_key(self, event):
        if event.keysym in ['e', 'BackSpace', 'equal', 'plus', 'minus', 'parenleft',
                            'parenright', 'slash', 'asterisk', 'c', 'C', '.', '1', '2',
                            '3', '4', '5', '6', '7', '8', '9', '0', 'Return']:
            self.logicalc(event.keysym)
            # print(event.keycode, event.char, event.keysym)

    def logicalc(self, operation):
        if operation in ['C', 'c']:
            self.formula = ""
        elif operation in ["⇐", 'BackSpace']:
            self.formula = self.formula[:-1]

        elif operation == "±":
            if self.formula[0] == '-':
                self.formula = self.formula[1:]
            else:
                self.formula = '-' + self.formula

        elif operation == "x²":
            if self.formula.endswith(('/', '*', "+", '-')):
                self.formula = self.formula[:-1]
            self.formula = str((eval(self.formula)) ** 2)

        elif operation == '√':
            if self.formula.endswith(('/', '*', "+", '-')):
                self.formula = self.formula[:-1]
            self.formula = str(sqrt(eval(self.formula)))

        elif operation == 'e':
            if self.formula.endswith(('/', '*', "+", '-')):
                self.formula += str(e)
            if self.formula == '0' or any(i not in self.formula for i in ['-', '*', '/', '+', '(', ')']):
                self.formula = str(e)

        elif operation == 'π':
            if self.formula.endswith(('/', '*', "+", '-')):
                self.formula += str(pi)
            if self.formula == '0' or any(i not in self.formula for i in ['-', '*', '/', '+', '(', ')']):
                self.formula = str(pi)

        elif operation == 'lg':
            if not self.formula.endswith(('/', '*', "+", '-')):
                self.formula = str(log10(eval(self.formula)))

        elif operation == 'ln':
            if not self.formula.endswith(('/', '*', "+", '-')):
                self.formula = str(log(eval(self.formula), e))

        elif operation == 'n!':
            if not self.formula.endswith(('/', '*', "+", '-')):
                if eval(self.formula) < 50:
                    self.formula = str(factorial(eval(self.formula)))
                else:
                    self.formula = 'error'

        elif operation in ["=", 'Return', 'equal']:
            try:
                if self.formula.endswith(('/', '*', "+", '-')):
                    self.formula = self.formula[:-1]
                self.formula = str(eval(self.formula))
            except ZeroDivisionError:
                self.formula = '0'
        else:
            if self.formula == "0" or self.formula == '/' or self.formula == '*':
                self.formula = ""
            self.formula += operation

        self.update()

    def update(self):
        self.formula = self.formula.replace('plus', '+')
        self.formula = self.formula.replace('minus', '-')
        self.formula = self.formula.replace('slash', '/')
        self.formula = self.formula.replace('asterisk', '*')
        self.formula = self.formula.replace('parenleft', '(')
        self.formula = self.formula.replace('parenright', ')')
        if self.formula.endswith('.0'):
            self.formula = self.formula.replace('.0', '')

        if self.formula in ['/', '*', "+", '']:
            self.formula = '0'

        if self.formula.endswith(('--', '++', '//', '**', '/+', '/*', '/-', '+/', '+*', '+-', '-+', '-/',
                                  '-*', '*-', '*+', '*/', '-)', '+)', '/)', '*)', '(+', '(*', '(/')):
            self.formula = self.formula[:-1]

        elif self.formula.count('(') < self.formula.count(')'):
            self.formula = self.formula[:-1]

        elif re.match('\d\(', self.formula[-2:]) or re.match('\)\d', self.formula[-2:]):
            self.formula = self.formula[:-1]

        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#FFF"
    root.geometry("340x520+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
