__author__ = 'dima'

from tkinter import *


class PreprocessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=800, height=600)
        self.pack()
        self.master.title('Окно препроцессора')

        self.make_widgets()

    def make_widgets(self):
        self.top_frame = Frame(self, width=640, height=480)
        self.top_frame.grid(row=0, column=0)

        self.bottom_frame = Frame(self, width=640, height=120)
        self.bottom_frame.grid(row=1, column=0)

        self.right_frame = Frame(self, width=160, height=600)
        self.right_frame.grid(row=0, column=1, rowspan=2)

        self.construction = Canvas(self.top_frame, width=640, height=480, bg='white')
        self.construction.pack(fill=BOTH)

        self.draw_btn = Button(self.right_frame, text='О\n'
                                                      'Т\n'
                                                      'Р\n'
                                                      'И\n'
                                                      'С\n'
                                                      'О\n'
                                                      'В\n'
                                                      'А\n'
                                                      'Т\n'
                                                      'Ь\n',
                                font=('Verdana', 14, 'italic bold'),
                                command=self.draw)

        self.draw_btn.pack(side=TOP, expand=YES, fill=BOTH)

        self.open_btn = Button(self.bottom_frame, text='Открыть файл', font=('Verdana', 10, 'italic bold'),
                               command=self.open_file)
        self.open_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.save_btn = Button(self.bottom_frame, text='Сохранить в файл', font=('Verdana', 10, 'italic bold'),
                               command=self.save_file)
        self.save_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.param_btn = Button(self.bottom_frame, text='Параметры конструкции', font=('Verdana', 10, 'italic bold'),
                               command=self.read_parameters)
        self.param_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.force_btn = Button(self.bottom_frame, text='Нагрузки', font=('Verdana', 10, 'italic bold'),
                               command=self.read_forces)
        self.force_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.about_btn = Button(self.bottom_frame, text='О программе', font=('Verdana', 10, 'italic bold'),
                               command=self.about_win)
        self.about_btn.pack(side=LEFT, expand=YES, fill=BOTH)

    def draw(self):
        pass

    def open_file(self):
        pass

    def save_file(self):
        pass

    def read_parameters(self):
        pass

    def read_forces(self):
        pass

    def about_win(self):
        pass