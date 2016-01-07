__author__ = 'dima'

from tkinter import *


class ProcessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title('Процессор')
        self.pack()

        self.cv = Canvas(self, bg='#FFFFFF', width=500, height=300)
        self.btns_frame = Frame(self)
        self.calc_btn = Button(self.btns_frame, text='Рассчитать', font=('Times', 10, 'italic bold'))
        self.show_matrix_btn = Button(self.btns_frame, text='Показать матрицу', font=('Times', 10, 'italic bold'),
                                      state=DISABLED)
        self.cancel_btn = Button(self.btns_frame, text='Отмена', font=('Times', 10, 'italic bold'))

        self.place_widgets()

    def place_widgets(self):
        self.calc_btn.pack(side=LEFT, expand=YES)
        self.show_matrix_btn.pack(side=LEFT, expand=YES)
        self.cancel_btn.pack(side=RIGHT, expand=YES)

        self.cv.pack(side=TOP)
        self.btns_frame.pack(side=BOTTOM, anchor=SE)


if __name__ == '__main__':
    ProcessorWin(Tk()).mainloop()