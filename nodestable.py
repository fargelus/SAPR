__author__ = 'dima'


from generaltable import Tablebuttons, Table, Entrysnodes
from tkinter import *
from savedata import save_nodes
from tkinter.messagebox import showerror, showwarning
from tkinter.simpledialog import askinteger
import rodstable


class Nodestable(Frame):
    count = 0
    dict_items = dict()

    @staticmethod
    def get_data_about_nodes():
        return Nodestable.dict_items

    @staticmethod
    def set_dict(data):
        if Nodestable.dict_items:
            Nodestable.dict_items.clear()

        for item in data:
            key = item[0]
            val = item[1:]
            Nodestable.dict_items[key] = val

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.columns = ('№', 'F', 'Заделка')
        self.tbl = Table(self, title='Узлы', columns=('№', 'F', 'Заделка'))
        self.tbl.table_tree['show'] = 'headings'

        self.entr = Entrysnodes(self)
        self.btns = Tablebuttons(self)

        self.btns.plus_btn.bind('<Button-1>', self.add_new_node)
        self.btns.minus_btn.bind('<Button-1>', self.delete_node)
        self.btns.save_btn.bind('<Button-1>', self.save_all)
        self.entr.ready_btn.bind('<Button-1>', self.fetch_res)

        self.place_widgets()

        if Nodestable.dict_items:
            self.setter_nodes()

    def fetch_res(self, event):
        if self.entr.numb_entry.get():
            try:
                number_node = int(self.entr.numb_entry.get())
                if number_node <= 0:
                    showwarning('Предупреждение', 'Номер узла должен быть > 0', parent=self)
                    self.entr.numb_entry.delete(0, END)
            except ValueError:
                showerror('Ошибка', 'Значение должно быть целочисленным', parent=self)
                self.entr.numb_entry.delete(0, END)
                return
        else:
            showerror('Ошибка', 'Не введен № узла', parent=self)
            if self.entr.force_entrys.get():
                self.entr.force_entrys.delete(0, END)
            return

        if self.entr.force_entrys.get():
            try:
                force = int(self.entr.force_entrys.get())
            except ValueError:
                showerror('Ошибка', 'Значение должно быть целочисленным', parent=self)
                self.entr.force_entrys.delete(0, END)
                return
        else:
            force = 0

        check_block = self.entr.var.get()

        if number_node in Nodestable.dict_items.keys():
            Nodestable.dict_items[number_node] = (force, check_block)
            if number_node <= Nodestable.count:
                self.clear_table()
                self.fill_table()
            else:
                self.tbl.table_tree.delete(number_node)
                self.tbl.table_tree.insert('', number_node, iid=int(number_node),
                                           values=(number_node, force, check_block))

        else:
            if number_node > Nodestable.count:
                for i in range(Nodestable.count + 1, number_node):
                    Nodestable.dict_items[i] = (0, 0)
                    self.tbl.table_tree.insert('', i, values=(i, 0, 0))

            Nodestable.dict_items[number_node] = (force, check_block)
            self.tbl.table_tree.insert('', number_node, values=(number_node, force, check_block))

        Nodestable.count = len(Nodestable.dict_items)
        self.set_vals_on_center()

    def place_widgets(self):
        self.tbl.pack()
        self.btns.pack(anchor=SE)
        self.entr.pack(anchor=W, pady=4)

    def add_new_node(self, event):
        Nodestable.count += 1

        self.tbl.table_tree.insert('', 'end', iid=Nodestable.count, values=(Nodestable.count, 0, 0))

        self.set_vals_on_center()

        Nodestable.dict_items[Nodestable.count] = (0, 0)

    def clear_table(self):
        self.tbl.table_tree.delete(*self.tbl.table_tree.get_children())

    def fill_table(self):
        for key in sorted(Nodestable.dict_items):
            val1, val2 = Nodestable.dict_items[key]
            self.tbl.table_tree.insert('', 'end', iid=key, values=(key, val1, val2))

    def delete_node(self, event):
        if Nodestable.count == 0:
            showerror('Ошибка удаления', 'В таблице не осталось заполненных полей')
            return

        number_to_del = askinteger('', 'Введите № узла:', parent=self)
        if number_to_del not in Nodestable.dict_items:
            showwarning('Предупреждение', 'Вы пытаетесь удалить узел, которого '
                                          'не существует', parent=self)
            return

        self.clear_table()

        Nodestable.dict_items.pop(number_to_del)
        Nodestable.count -= 1
        for item in Nodestable.dict_items:
            if item > number_to_del:
                Nodestable.dict_items[item - 1] = (Nodestable.dict_items[item][0],
                                                   Nodestable.dict_items[item][1])
                Nodestable.dict_items.pop(item)

        self.fill_table()

    def set_vals_on_center(self):
        for col in self.columns:
            self.tbl.table_tree.column(col, anchor=CENTER)

    def setter_nodes(self):
        Nodestable.count = len(Nodestable.dict_items)
        self.clear_table()

        self.fill_table()

        self.set_vals_on_center()

    def save_all(self, event):
        if rodstable.Rodstable.dict_items:
            if len(Nodestable.dict_items) - len(rodstable.Rodstable.dict_items) != 1:
                showerror('Ошибка', 'Кол-во узлов должно быть на единицу больше кол-ва стержней', parent=self)
                self.tbl.table_tree.delete(*self.tbl.table_tree.get_children())
                Nodestable.dict_items = dict()
                Nodestable.count = 0
            else:
                save_nodes(Nodestable.dict_items)
        else:
            save_nodes(Nodestable.dict_items)

if __name__ == '__main__':
    Nodestable().mainloop()