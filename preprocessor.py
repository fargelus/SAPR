__author__ = 'dima'

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


class PreprocessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.master.title('Окно препроцессора')

        self.make_widgets()

    def make_widgets(self):
        Innerframe(self).pack(side=BOTTOM)
        Construction(self).pack(side=LEFT)
        Drawbutton(self).pack(side=RIGHT)



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


class Drawbutton(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)

        self.btn = Button(self, text='О\n'
                          'Т\n'
                          'Р\n'
                          'И\n'
                          'С\n'
                          'О\n'
                          'В\n'
                          'А\n'
                          'Т\n'
                          'Ь\n',
                      font=('Times', 14, 'italic bold')).pack(expand=YES, fill=BOTH)

        #self.master.config(width=160, height=600)


class Innerframe(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=640, height=120)
        self.pack(expand=YES, fill=BOTH)

        self.make_widgets()

    def make_widgets(self):
        self.opn_file_btn = Button(self, text='Открыть файл', font=('Times', 10, 'italic bold'),
                                command=self.open_file)
        self.opn_file_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.save_file_btn = Button(self, text='Сохранить в файл', font=('Times', 10, 'italic bold'),
                                    command=self.save_file)
        self.save_file_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.param_btn = Button(self, text='Параметры конструкции', font=('Times', 10, 'italic bold'))
                               # command=self.open_param_win)
        self.param_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.force_btn = Button(self, text='Нагрузки', font=('Times', 10, 'italic bold'))
                               # command=self.open_force_win)
        self.force_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.about_btn = Button(self, text='О программе', font=('Times', 10, 'italic bold'),
                                command=self.about)
        self.about_btn.pack(side=LEFT, expand=YES, fill=BOTH)

    def open_file(self):
        filename = askopenfilename(parent=self, defaultextension='.db', filetypes=[('Database', '.db'),
                                                                                   ('SQLite3', '.sqlite3'),
                                                                                   ('SQLite', '.sqlite')],
                                   initialdir='/home/dima/Рабочий стол/САПР/Computer Mechanic/data')
        print(filename)

    def save_file(self):
        filename = asksaveasfilename(parent=self, defaultextension='.db', filetypes=[('Database', '.db'),
                                                                                   ('SQLite3', '.sqlite3'),
                                                                                   ('SQLite', '.sqlite')],
                                   initialdir='/home/dima/Рабочий стол/САПР/Computer Mechanic/data')
        print(filename)


    def about(self):
        showinfo('Справка', '')


class Construction(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.cv = Canvas(self, width=640, height=480, bg='white')
        self.cv.pack(expand=YES, fill=BOTH)

        self.cv.create_text(300, 25, text='Конструкция', fill='gray', font=('Times', 15, 'italic bold'))
