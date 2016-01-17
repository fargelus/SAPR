__author__ = 'dima'

from tkinter import *
# from nodestable import Nodestable
# from rodstable import Rodstable
from savedata import get_data


class ProcessorWin(Frame):

    _ = float('inf')

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title('Процессор')
        self.pack()

        self.cv = Canvas(self, bg='#FFFFFF', width=500, height=300)
        self.btns_frame = Frame(self)
        self.calc_btn = Button(self.btns_frame, text='Рассчитать', font=('Times', 10, 'italic bold'))
        self.show_matrix_btn = Button(self.btns_frame, text='Показать матрицу', font=('Times', 10, 'italic bold'),
                                      state=DISABLED)
        self.cancel_btn = Button(self.btns_frame, text='Отмена', font=('Times', 10, 'italic bold'),
                                 command=self.master.destroy)

        self.calc_btn.bind('<Button-1>', self.calculate)

        self.place_widgets()

    def place_widgets(self):
        self.calc_btn.pack(side=LEFT, expand=YES)
        self.show_matrix_btn.pack(side=LEFT, expand=YES)
        self.cancel_btn.pack(side=RIGHT, expand=YES)

        self.cv.pack(side=TOP)
        self.btns_frame.pack(side=BOTTOM, anchor=SE)

    def calculate(self, event):
        self.cv.create_text(85, 10, text='Обработка результатов...')

        # желательно прикрутить здесь progressbar
        self.cv.after(2500, lambda: None)
        self.solution()
        self.cv.create_text(28, 25, text='Готово')
        self.show_matrix_btn['state'] = NORMAL

    def solution(self):
        _ = ProcessorWin._

        rods, nodes = get_data('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/test.db')

        l_list = [val[1] for val in rods]
        a_list = [val[2] for val in rods]
        e_list = [val[3] for val in rods]

        # p - номер стержня
        # i - номер глобального узла
        # n - число глобальных узлов
        n = len(nodes)
        A = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j or i + 1 == j or i - 1 == j:
                    A[i][j] = _

        # плохо - переделать!
        # формирование глобальной матрицы реакций А(EA/L)
        for i in range(n):
            for j in range(n):
                if A[i][j] == _:
                    if i == j:
                        if i == 0 or i == n - 1:
                            if i == 0:
                                A[i][j] = e_list[0] * a_list[0] / l_list[0]
                            else:
                                A[i][j] = e_list[-1] * a_list[-1] / l_list[-1]
                        else:
                            A[i][j] = (e_list[i - 1] * a_list[i - 1] / l_list[i - 1]) + \
                                      (e_list[i] * a_list[i] / l_list[i])
                    else:
                        if i > j:
                            A[i][j] = -(e_list[i - 1] * a_list[i - 1] / l_list[i - 1])
                        else:
                            A[i][j] = -(e_list[j - 1] * a_list[j - 1] / l_list[j - 1])

        print(rods)
        print()
        print(nodes)

        # формирование глобального вектора реакций b
        b = []
        for val in rods:
            sum_q = 0
            index = rods.index(val)
            for i in range(index, -1, -1):
                q = val[-1]
                l = l_list[index]
                sum_q += -q * l / 2
            item = sum_q + nodes[index][1]
            b.append(item)
            if index == len(rods) - 1:
                b.append(sum_q + nodes[index + 1][1])

        # изменение матрицы А с учётом заделок
        row_to_operate = []
        for val in nodes:
            index = nodes.index(val)
            if val[-1] != 0:
                for i in range(n):
                    if index == i:
                        A[index][i] = 1
                    else:
                        A[index][i] = 0
            else:
                row_to_operate.append(index)

        move = [0 if val[1] == 0 else 1 for val in nodes]
        equation = dict()
        for row in row_to_operate:
            sum_row = ""
            for j in range(n):
                if j in row_to_operate:
                    sum_row += str(A[row][j]) + ' '
            equation[sum_row] = b[row]

        if len(equation) == 1:
            index = row_to_operate[0]
            key = A[index][index]
            move[index] = key / equation[str(key) + ' ']
        else:
            pass

        print(move)













if __name__ == '__main__':
    ProcessorWin(Tk()).mainloop()
