__author__ = 'dima'

from tkinter import *


class PostprocessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title('Постпроцессор')
        self.pack()

        self.inner_fr = Frame(self)
        self.nx_btn = Button(self.inner_fr, text='График Nx', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.ux_btn = Button(self.inner_fr, text='График U', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.sigmax_btn = Button(self.inner_fr, text='График σ', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.tbl_btn = Button(self.inner_fr, text='Показать таблицу', font=('Times', 10, 'italic bold'),
                              bd=5, relief=FLAT)

        self.report_btn = Button(self.inner_fr, text='Показать файл рез-та расчёта', font=('Times', 10, 'italic bold'),
                                 bd=5, relief=FLAT)

        self.diagram_btn = Button(self.inner_fr, text='Отобразить эпюры', font=('Times', 10, 'italic bold'),
                                  bd=5, relief=FLAT)

        self.place_widgets()

    def place_widgets(self):
        self.inner_fr.pack(expand=YES, fill=BOTH)

        self.nx_btn.pack(side=TOP, fill=X, expand=YES)
        self.ux_btn.pack(side=TOP, fill=X, expand=YES)
        self.sigmax_btn.pack(side=TOP, fill=X, expand=YES)
        self.tbl_btn.pack(side=TOP, fill=X, expand=YES)
        self.report_btn.pack(side=TOP, fill=X, expand=YES)
        self.diagram_btn.pack(side=TOP, fill=X, expand=YES)


if __name__ == '__main__':
    PostprocessorWin(Tk()).mainloop()

