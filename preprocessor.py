__author__ = 'dima'

from tkinter import *
from mainwindow import AbstractWindow, FONT, COLOR


class Preprocessorbutton(Button):
    def __init__(self, parent=None, **options):
        Button.__init__(self, parent, options)
        self.config(text='Препроцессор', font=FONT)
        self.bind('<Button-1>', lambda event: self.on_btn_click())

    def on_btn_click(self):
        win = Toplevel()
        child = Preprocessorwin(win)
        child.mainloop()


class Preprocessorwin(AbstractWindow):
    def __init__(self, parent=None):
        AbstractWindow.__init__(self, parent, color=COLOR)
        self.pack()
        self.master.title('Окно препроцессора')
        self.make_widgets()

    def make_widgets(self):
        fr = Frame(self, width=180, height=150, bg=COLOR)
        fr.pack()
        self.cv.create_window(320, 250, window=fr)

        param_btn = Parametersbutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        param_btn.pack(expand=YES, fill=BOTH)

        force_btn = Forcebutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        force_btn.pack(expand=YES, fill=BOTH, pady=5)

        draw_btn = Drawbutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        draw_btn.pack(expand=YES, fill=BOTH)


class Parametersbutton(Button):
    def __init__(self, parent=None, **kwargs):
        Button.__init__(self, parent, kwargs)
        self.pack()

        self.config(text='Параметры', font=FONT)
        self.bind('<Button-1>', lambda event: self.on_param_btn_click())

    def on_param_btn_click(self):
        win = Toplevel()
        child = Parameterswin(win)
        child.mainloop()


class Parameterswin(AbstractWindow):
    def __init__(self, parent=None):
        AbstractWindow.__init__(self, parent)
        self.pack()
        self.master.title('Окно параметров')
        self.make_widgets()

    def make_widgets(self):
        mainframe = Frame(self, width=450, height=350)
        mainframe.pack()
        self.cv.create_window(320, 225, window=mainframe)

        btn_frame = Frame(self, width=350, height=80, bg='white')
        btn_frame.pack()
        self.cv.create_window(450, 440, window=btn_frame)

        del_btn = Button(btn_frame, text='Удалить', font=FONT)
        del_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        add_btn = Button(btn_frame, text='Добавить', font=FONT)
        add_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        ready_btn = Button(btn_frame, text='Готово', font=FONT)
        ready_btn.pack(expand=YES, fill=BOTH)


class Forcebutton(Button):
    def __init__(self, parent=None, **kwargs):
        Button.__init__(self, parent, kwargs)
        self.pack()

        self.config(text='Нагрузки', font=FONT)
        self.bind('<Button-1>', lambda event: self.on_force_btn_click())

    def on_force_btn_click(self):
        pass


class Drawbutton(Button):
    def __init__(self, parent=None, **kwargs):
        Button.__init__(self, parent, kwargs)
        self.pack()

        self.config(text='Отрисовка конструкции', font=FONT)
        self.bind('<Button-1>', lambda event: self.on_draw_btn_click())

    def on_draw_btn_click(self):
        pass
