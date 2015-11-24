__author__ = 'dima'

from tkinter import *
from tkinter.ttk import Treeview


GENERAL_FONT = ('Times', 12, 'italic bold')


class Readybutton(Button):
    def __init__(self, parent=None):
        Button.__init__(self, parent, text='Готово', font=GENERAL_FONT)


class Entrysrods(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)

        self.numb_lbl = Label(self, text='№:')
        self.numb_entry = Entry(self, width=30)

        self.length_lbl = Label(self, text='L:')
        self.length_entry = Entry(self, width=30)

        self.e_lbl = Label(self, text='E:')
        self.e_entry = Entry(self, width=30)

        self.a_lbl = Label(self, text='A:')
        self.a_entry = Entry(self, width=30)

        self.sigma_lbl = Label(self, text='[σ]:')
        self.sigma_entry = Entry(self, width=30)

        self.q_lbl = Label(self, text='q:')
        self.q_entry = Entry(self, width=30)

        self.ready_btn = Readybutton(self)

        self.place_widgets()

    def place_widgets(self):
        self.numb_lbl.grid(row=0, column=0)
        self.numb_entry.grid(row=0, column=1, padx=10)

        self.length_lbl.grid(row=1, column=0)
        self.length_entry.grid(row=1, column=1)

        self.e_lbl.grid(row=2, column=0)
        self.e_entry.grid(row=2, column=1)

        self.a_lbl.grid(row=0, column=3)
        self.a_entry.grid(row=0, column=4)

        self.sigma_lbl.grid(row=1, column=3)
        self.sigma_entry.grid(row=1, column=4)

        self.q_lbl.grid(row=2, column=3)
        self.q_entry.grid(row=2, column=4)

        self.ready_btn.grid(row=3, column=4, rowspan=2, sticky=SE)


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


class Entrysnodes(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.numb_lbl = Label(self, text='№:')
        self.numb_entry = Entry(self, width=20)

        self.force_lbl = Label(self, text='F:')
        self.force_entrys = Entry(self, width=20)

        self.obstacle_check = Checkbutton(self, text='Заделка')
        self.ready_btn = Readybutton(self)

        self.place_widgets()

    def place_widgets(self):
        self.numb_lbl.grid(row=0, column=0)
        self.numb_entry.grid(row=0, column=1)

        self.force_lbl.grid(row=2, column=0)
        self.force_entrys.grid(row=2, column=1)

        self.obstacle_check.grid(row=1, column=2, padx=10)

        self.ready_btn.grid(row=4, column=2, sticky=SE)


class Table(Frame):
    def __init__(self, parent, title, columns, columns_names):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.title_lbl = Label(self, text=title, font=GENERAL_FONT)
        self.table_tree = Treeview(self, columns=columns)

        self.table_tree.heading('#0', text=columns_names[0])

        for i in range(len(columns)):
            self.table_tree.heading(columns[i], text=columns_names[i+1])

        self.place_widgets()

    def place_widgets(self):
        self.title_lbl.pack(side=TOP, fill=X, expand=YES)
        self.table_tree.pack(side=LEFT, fill=BOTH, expand=YES)


if __name__ == '__main__':
    Entrysnodes().mainloop()

