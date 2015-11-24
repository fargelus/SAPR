__author__ = 'dima'


from generaltable import Tablebuttons, Table, Entrysnodes
from tkinter import *


class Nodestable(Frame):
    count = 0

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.tbl = Table(self, title='Узлы', columns=('F', 'Заделка'),
                         columns_names=('№', 'F', 'Заделка'))

        self.entr = Entrysnodes(self)
        self.btns = Tablebuttons(self)

        self.place_widgets()

    def place_widgets(self):
        self.tbl.pack()
        self.btns.pack(anchor=SE)
        self.entr.pack(anchor=W, pady=4)


    def add_new_node(self):
        pass

    def delete_node(self):
        pass

    def save_all(self):
        pass


if __name__ == '__main__':
    Nodestable().mainloop()