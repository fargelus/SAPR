__author__ = 'dima'

""" графики для постпроцессора """

from tkinter import *
import sqlite3 as lite
from savedata import get_data


class General(Frame):
    """ общий класс графиков """
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()

        self.cv = Canvas(self, width=640, height=480, bg='#FFFFFF')
        self.cv.create_line(60, 80, 60, 400)
        self.cv.create_line(40, 240, 600, 240)
        self.cv.create_line(580, 80, 580, 400)
        self.cv.pack()


class NxGraphic(General):
    def __init__(self, parent=None):
        General.__init__(self, parent)
        self.pack()

        self.master.title('График Nx')

        con = lite.connect('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res.db')
        with con:
            cur = con.cursor()
            self.data = tuple(cur.execute('SELECT * FROM Nx'))

        filename = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/filepath.txt').readline().strip()
        self.rods = get_data(filename)[0]

        self.draw_graphic()

    def draw_graphic(self):
        l_list = [val[1] for val in self.rods]

        diff_x = 520
        start_x = 60
        start_y = 80
        end_y = 400
        end_x = 580

        all_parts = sum(l_list)
        shifts = []
        for item in l_list:
            shift_x = start_x + diff_x * item // all_parts
            if shift_x > end_x:
                shift_x = end_x
            if end_x - shift_x <= 10:
                shift_x = end_x
            start_x = shift_x
            temp_y = start_y
            while temp_y <= end_y:
                self.cv.create_line(shift_x, temp_y, shift_x, temp_y + 5)
                temp_y += 10
            shifts.append(start_x)

        start_x = 60
        for each in self.data:
            index, val = each
            if start_x > diff_x / 2:
                self.cv.create_text(end_x + 20, 240 - int(val), text='%s' % val)
            else:
                self.cv.create_text(40, 240 - int(val), text='%s' % val)
            self.cv.create_line(start_x, 240 - int(val), shifts[index - 1], 240 - int(val))

            while start_x < shifts[index - 1]:
                if start_x + 10 > shifts[index - 1]:
                    break
                start_x += 10
                self.cv.create_line(start_x, 240, start_x, 240 - int(val))
            if start_x != shifts[index - 1]:
                start_x = shifts[index - 1]


class UxGraphic(General):
    def __init__(self, parent=None):
        General.__init__(self, parent)
        self.pack()

        self.master.title('График Ux')


class SigmaGraphic(General):
    def __init__(self, parent=None):
        General.__init__(self, parent)
        self.pack()

        self.master.title('График Sigma')


if __name__ == '__main__':
    NxGraphic(Tk()).mainloop()