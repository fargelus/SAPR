__author__ = 'dima'

from tkinter import *
# from rodstable import Rodstable
# from nodestable import Nodestable
from savedata import get_data
from os import getcwd


class Drawbutton(Frame):

    middle = int()

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)

        self.cv = Canvas(self, width=640, height=480, bg='white')
        self.cv.pack(side=LEFT, expand=YES, fill=BOTH)

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
                      font=('Times', 14, 'italic bold'))

        self.btn.pack(expand=YES, fill=BOTH, side=RIGHT)
        self.btn.bind('<Button-1>', self.draw)

    def draw(self, event):
        initial_dir = getcwd()
        rods, nodes = get_data(initial_dir + '/data/test.db')
        print(rods)
        print()
        print(nodes)

        begin_x = 50
        begin_y = 240
        nodes_coord = []
        h = int()
        for item in rods:
            l = 100 * item[1]
            h = (item[2] * 5000) / l
            index = rods.index(item)

            if index == 0:
                Drawbutton.middle = begin_y + h / 2
            if index >= 1:
                begin_y = Drawbutton.middle - (h / 2)

            nodes_coord.append([begin_x, begin_y, h])

            self.cv.create_rectangle(begin_x, begin_y, begin_x + l, begin_y + h)
            self.draw_number_rod(index, nodes_coord[index], l)
            self.draw_l_line(nodes_coord[index], l)
            self.draw_ea_line(nodes_coord[index], l, item[2], item[3])
            begin_x += l

        nodes_coord.append([begin_x, begin_y, h])
        self.draw_axes_system(nodes_coord)

        for val in nodes:
            index = nodes.index(val)
            if val[1] != 0:
                self.draw_force(nodes_coord[index], val[1], index)
            if val[2] != 0:
                self.draw_block(nodes_coord[index], index)
            self.draw_number_node(nodes_coord[index], index)

    def draw_force(self, coords, value, index):
        x = coords[0]
        y = Drawbutton.middle
        if value > 0:
            self.cv.create_line(x, y, x + 50, y, arrow=LAST)
            self.cv.create_text(x + 25, y - 10, text='F%s=%s' % (index + 1, value))
        else:
            self.cv.create_line(x, y, x - 50, y, arrow=LAST)
            self.cv.create_text(x - 25, y - 10, text='F%s=%s' % (index + 1, value))

    def draw_block(self, coords, numb_node):
        x, y, shift = coords
        if not isinstance(y, int):
            y = int(y)
        if not isinstance(shift, int):
            shift = int(shift)

        end = y + shift + 10
        self.cv.create_line(x, y - 10, x, end)
        if numb_node == 0:
            for i in range(y - 10, end, 5):
                self.cv.create_line(x, i, x - 5, i + 5)
        else:
            for i in range(end, y - 10, -5):
                self.cv.create_line(x, i, x + 5, i - 5)

    def draw_number_rod(self, index, coords, l):
        x = coords[0]
        x += l / 3
        y = 150         # плохо, переделать

        self.cv.create_oval(x, y, x + 25, y + 25)
        self.cv.create_text(x + 12, y + 12, text='%s' % (index + 1))

    def draw_number_node(self, coords, value):
        x, y, shift = coords
        y += (shift + 15)
        self.cv.create_rectangle(x, y, x + 15, y + 15)
        self.cv.create_text(x + 7, y + 7, text='%s' % (value + 1))

    def draw_l_line(self, coords, l):
        l_to_draw = l // 100
        x, y, shift = coords
        y += shift
        self.cv.create_line(x, y, x, y + 50)
        save_x = x
        x += l
        self.cv.create_line(x, y, x, y + 50)
        self.cv.create_line(save_x, y + 35, x, y + 35, arrow=BOTH)
        self.cv.create_text(save_x + l/2, y + 25, text='%sL' % l_to_draw)

    def draw_ea_line(self, coords, l, a_val, e_val):
        x, y, shift = coords
        x += l/2
        y += 10
        self.cv.create_line(x, y, x + 20, y - 20)
        x += 20
        y -= 20
        self.cv.create_line(x, y, x + 40, y)
        self.cv.create_text(x + 20, y - 10, text='%sE, %sA' % (e_val, a_val))

    def draw_axes_system(self, coords):
        begin_x = coords[0][0] - 20
        end_x = coords[-1][0] + 30
        y = Drawbutton.middle
        while begin_x <= end_x:
            if begin_x + 10 > end_x:
                self.cv.create_line(begin_x, y, begin_x + 5, y, arrow=LAST)
            else:
                self.cv.create_line(begin_x, y, begin_x + 5, y)
            begin_x += 10
        self.cv.create_text(end_x, y + 10, text='X')

        begin_y = coords[0][1]
        x = coords[0][0]
        end_y = 50
        while begin_y >= end_y:
            if begin_y - 10 < end_y:
                self.cv.create_line(x, begin_y, x, begin_y - 5, arrow=LAST)
            else:
                self.cv.create_line(x, begin_y, x, begin_y - 5)
            begin_y -= 10
        self.cv.create_text(x + 10, end_y, text='Y')


if __name__ == '__main__':
    Drawbutton().mainloop()