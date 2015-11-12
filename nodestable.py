__author__ = 'dima'

from generaltable import *


class Nodestable(Table):
    count = 0

    def __init__(self, parent=None):
        Table.__init__(self, parent, 'Узлы', columns=('Заделка', 'F'),
                       columns_names=('№ узла','Заделка', 'F'))
        self.master.title('Параметры узлов')

        self.btns.plus_btn.bind('<Button-1>', lambda event: self.add_new_node())
        self.btns.minus_btn.bind('<Button-1>', lambda event: self.delete_node())
        self.btns.save_btn.bind('<Button-1>', lambda event: self.save_all())

        self.pack()

    def add_new_node(self):
        pass

    def delete_node(self):
        pass

    def save_all(self):
        pass



if __name__ == '__main__':
    Nodestable().mainloop()
