__author__ = 'dima'

from generaltable import *
from tkinter.simpledialog import askinteger
from tkinter.messagebox import showerror, showwarning
from copy import copy


class Rodstable(Table):

    # статическая переменная счётчик
    count = 0

    def __init__(self, parent=None):
        Table.__init__(self, parent, 'Стержни', columns=('L', 'A', 'E', 'σ', 'q'),
                       columns_names=('№ стержня', 'L', 'A', 'E', 'σ', 'q'))
        self.master.title('Параметры стержней')

        self.btns.plus_btn.bind('<Button-1>', self.add_new_rode)
        self.btns.minus_btn.bind('<Button-1>', self.delete_rode)
        self.btns.save_btn.bind('<Button-1>', self.save_all)

        self.dict_items = dict()
        self.pack()

    def get_length(self):
        length = askinteger('Введите длину стержня', 'Длина:')
        while length <= 0:
            showerror('Ошибка ввода', 'Значение длины должно быть > 0')
            length = askinteger('Введите длину стержня', 'Длина:')
        return length

    def get_s(self):
        s = askinteger('Введите площадь стержня', 'Площадь:')
        while s <= 0:
            showerror('Ошибка ввода', 'Значение площади должно быть > 0')
            s = askinteger('Введите площадь стержня', 'Площадь:')
        return s

    def get_module_young(self):
        module_young = askinteger('Введите модуль Юнга', 'Значение:')
        while module_young < 0:
            showerror('Ошибка ввода', 'Значение модуля Юнга должно быть >= 0')
            module_young = askinteger('Введите модуль Юнга', 'Значение:')
        return module_young

    def get_sigma(self):
        sigma = askinteger('Введите допускаемое напряжение', 'Значение:')
        while sigma <= 0:
            showerror('Ошибка ввода', 'Значение напряжения должно быть > 0')
            sigma = askinteger('Введите допускаемое напряжение', 'Значение:')
        return sigma

    def get_q(self):
        q = askinteger('Введите значение распределенной нагрузки', 'Значение:')
        while q < 0:
            showerror('Ошибка ввода', 'Значение нагрузки должно быть >= 0')
            q = askinteger('Введите значение распределенной нагрузки', 'Значение:')
        return q

    def add_new_rode(self, event):
        length = self.get_length()
        s = self.get_s()
        module_young = self.get_module_young()
        sigma = self.get_sigma()
        q = self.get_q()

        # static count ?
        self.count += 1
        id = self.table_tree.insert('', 'end', text=str(self.count), values=(length,
                                                                        s, module_young,
                                                                        sigma, q),
                                    iid=self.count)
        self.dict_items[int(id)] = (length, s, module_young, sigma, q)

    def delete_rode(self, event):
        number = askinteger('Введите номер стержня', '№:')
        if number not in self.dict_items.keys():
            showwarning('Внимание', 'Такого стержня не существует')
        #self.table_tree.delete(number)
        copy_dict = copy(self.dict_items)

        for item in copy_dict:
            self.table_tree.delete(item)

        size = len(copy_dict)
        #self.dict_items.pop(number)
        self.dict_items = dict()

        self.count -= 1
        for i in range(1, self.count + 1):
            if i < number:
                self.dict_items[i] = copy_dict[i]
            else:
                if i <= size - 1:
                    self.dict_items[i] = copy_dict[i + 1]

        copy_dict = dict()
        for item in sorted(self.dict_items):
            id = self.table_tree.insert('', 0, text=str(item), iid=item, values=self.dict_items[item])
            copy_dict[int(id)] = self.dict_items[item]
        self.dict_items = copy(copy_dict)


    def save_all(self):
        pass





if __name__ == '__main__':
    Rodstable().mainloop()