__author__ = 'dima'

from tkinter import *
from graphics import *
from mytable import *
from export_file import *
from tkinter.messagebox import showinfo


class PostprocessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title('Постпроцессор')
        self.pack()

        self.inner_fr = Frame(self)
        self.nx_btn = Button(self.inner_fr, text='График Nx', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.ux_btn = Button(self.inner_fr, text='График U', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.sigmax_btn = Button(self.inner_fr, text='График σ', font=('Times', 10, 'italic bold'), bd=5, relief=FLAT)

        self.tbl_btn = Button(self.inner_fr, text='Показать таблицы', font=('Times', 10, 'italic bold'),
                              bd=5, relief=FLAT)

        self.report_btn = Button(self.inner_fr, text='Показать файл рез-та расчёта', font=('Times', 10, 'italic bold'),
                                 bd=5, relief=FLAT)

        # events
        self.nx_btn.bind('<Button-1>', lambda event: NxGraphic(Toplevel()).mainloop())
        self.ux_btn.bind('<Button-1>', lambda event: UxGraphic(Toplevel()).mainloop())
        self.sigmax_btn.bind('<Button-1>', lambda event: SigmaGraphic(Toplevel()).mainloop())
        self.tbl_btn.bind('<Button-1>', self.show_table)
        self.report_btn.bind('<Button-1>', self.report)

        self.place_widgets()

    def place_widgets(self):
        self.inner_fr.pack(expand=YES, fill=BOTH)

        self.nx_btn.pack(side=TOP, fill=X, expand=YES)
        self.ux_btn.pack(side=TOP, fill=X, expand=YES)
        self.sigmax_btn.pack(side=TOP, fill=X, expand=YES)
        self.tbl_btn.pack(side=TOP, fill=X, expand=YES)
        self.report_btn.pack(side=TOP, fill=X, expand=YES)

    def report(self, event):
        write_result()
        showinfo('Инфо', 'Отчёты сформированы', parent=self)

    def show_table(self, event):
        app = QApplication(sys.argv)

        table = MyTable()
        table.show()

        app.exec_()


if __name__ == '__main__':
    PostprocessorWin(Tk()).mainloop()

