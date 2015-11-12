__author__ = 'dima'

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
from drawconstruction import Drawbutton


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

        self.param_btn = Button(self, text='Параметры стержней', font=('Times', 10, 'italic bold'))
                               # command=self.open_param_win)
        self.param_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.force_btn = Button(self, text='Параметры узлов', font=('Times', 10, 'italic bold'))
                               # command=self.open_force_win)
        self.force_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.about_btn = Button(self, text='Справка', font=('Times', 10, 'italic bold'),
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
        win = Toplevel(self)
        Aboutwin(win).mainloop()


class Construction(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.cv = Canvas(self, width=640, height=480, bg='white')
        self.cv.pack(expand=YES, fill=BOTH)

        self.cv.create_text(300, 25, text='Конструкция', fill='gray', font=('Times', 15, 'italic bold'))


class Aboutwin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=640, height=480)
        self.pack()
        self.master.title('Справка')

        self.make_widgets()

    def make_widgets(self):
        frame_btns = Frame(self)
        frame_btns.pack(side=LEFT, expand=YES, fill=BOTH)

        about_btn = Button(frame_btns, text='О программе', font=('Times', 12, 'italic bold'),
                           command=self.show_about_info)
        about_btn.pack(side=TOP, expand=YES, fill=BOTH)
        prepr_btn = Button(frame_btns, text='Препроцессор', font=('Times', 12, 'italic bold'),
                           command=self.show_prepr_info)
        prepr_btn.pack(side=TOP, expand=YES, fill=BOTH)
        pr_btn = Button(frame_btns, text='Процессор', font=('Times', 12, 'italic bold'),
                        command=self.show_pr_info)
        pr_btn.pack(side=TOP, expand=YES, fill=BOTH)
        postpr_btn = Button(frame_btns, text='Постпроцессор', font=('Times', 12, 'italic bold'),
                            command=self.show_postpr_info)
        postpr_btn.pack(side=TOP, expand=YES, fill=BOTH)

        self.frame_text = Frame(self)
        self.frame_text.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.text_widget = Text(self.frame_text)
        self.text_widget.pack(expand=YES, fill=BOTH)

    def show_about_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/about_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_prepr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/prepr_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_pr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/proc_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_postpr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/postproc_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)



