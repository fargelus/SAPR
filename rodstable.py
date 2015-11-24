__author__ = 'dima'


from generaltable import Table, Tablebuttons, Entrysrods
from tkinter.simpledialog import askinteger
from tkinter.messagebox import showerror, showwarning
from copy import copy
from tkinter import *


class Rodstable(Frame):
    # статическая переменная счётчик
    count = 0

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.tbl = Table(self, 'Стержни', columns=('L', 'A', 'E', 'σ', 'q'),
                         columns_names=('№ стержня', 'L', 'A', 'E', 'σ', 'q'))
        self.entr = Entrysrods(self)
        self.btns = Tablebuttons(self)

        self.place_widgets()

    def place_widgets(self):
        self.tbl.pack()
        self.btns.pack(anchor=SE)

    def add_new_rode(self, event):



        # static count ?
        self.count += 1
        # id = self.table_tree.insert('', 'end', text=str(self.count), values=(length,
        #                                                                 s, module_young,
        #                                                                 sigma, q),
        #                             iid=self.count)
        # self.dict_items[int(id)] = (length, s, module_young, sigma, q)

    def delete_rode(self, event):


        # self.table_tree.delete(number)
        copy_dict = copy(self.dict_items)

        for item in copy_dict:
            self.table_tree.delete(item)

        size = len(copy_dict)
        # self.dict_items.pop(number)
        self.dict_items = dict()

        # сдвигаем позиции в таблице
        self.count -= 1
        # for i in range(1, self.count + 1):
        #     if i < number:
        #         self.dict_items[i] = copy_dict[i]
        #     else:
        #         if i <= size - 1:
        #             self.dict_items[i] = copy_dict[i + 1]

        copy_dict = dict()
        for item in sorted(self.dict_items, reverse=True):
            id = self.table_tree.insert('', 0, text=str(item), iid=item, values=self.dict_items[item])
            print(id)
            copy_dict[int(id)] = self.dict_items[item]
        self.dict_items = copy(copy_dict)

    def save_all(self, event):
        # filename = getcwd() + '/data/rods.db'
        pass


if __name__ == '__main__':
    Rodstable().mainloop()