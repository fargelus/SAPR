__author__ = 'dima'

from tkinter import *
from tkinter.ttk import Treeview


GENERAL_FONT = ('Times', 12, 'italic bold')


class Tablebuttons(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.save_btn = Button(self, text='Сохранить', font=GENERAL_FONT)
        self.plus_btn = Button(self, text='+', font=GENERAL_FONT)
        self.minus_btn = Button(self, text='-', font=GENERAL_FONT)

        self.place_widgets()

    def place_widgets(self):
        self.save_btn.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.plus_btn.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.minus_btn.pack(side=RIGHT, expand=YES, fill=BOTH)


class Table(Frame):
    def __init__(self, parent, title, columns, columns_names):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.title_lbl = Label(self, text=title, font=GENERAL_FONT)
        self.table_tree = Treeview(self, columns=columns)
        self.btns = Tablebuttons()

        self.table_tree.heading('#0', text=columns_names[0])

        for i in range(len(columns)):
            self.table_tree.heading(columns[i], text=columns_names[i+1])

        self.place_widgets()

    def place_widgets(self):
        self.title_lbl.pack(side=TOP, fill=X, expand=YES)
        self.table_tree.pack(side=LEFT, fill=BOTH, expand=YES)
        self.btns.pack(side=RIGHT)
