__author__ = 'dima'

""" пробуем запрогать GUI по проекту Чеканина """

from tkinter import *
from preprocessor import *
from processor import *
from postprocessor import *


COLOR = '#E6E6FA'
WIDTH = 640
HEIGHT = 480
FONT = ('Verdana', 14, 'italic bold')


class AbstractWindow(Frame):
    def __init__(self, parent=None, color=COLOR):
        Frame.__init__(self, parent)
        self.pack()

        self.cv = Canvas(self, width=WIDTH, height=HEIGHT, bg=color)
        self.cv.pack()


class MainWindow(AbstractWindow):
    def __init__(self):
        AbstractWindow.__init__(self)
        self.master.title('Главное окно')
        self.pack()

        self.make_widgets()

    def make_widgets(self):
        fr = Frame(self, width=180, height=150, bg=COLOR)
        fr.pack()
        self.cv.create_window(320, 250, window=fr)

        self.prebtn = Button(fr, bg='#D3D3D3', text='Препроцессор',
                             font=FONT, bd=8, relief=RAISED, command=self.make_preprocessorwin)
        self.prebtn.pack(expand=YES, fill=BOTH)

        self.prbtn = Button(fr, bg='#D3D3D3', text='Процессор', font=FONT, bd=8, relief=RAISED)
        self.prbtn.pack(expand=YES, fill=BOTH, pady=5)

        self.postprbtn = Button(fr, bg='#D3D3D3', text='Постпроцессор', font=FONT, bd=8, relief=RAISED)
        self.postprbtn.pack(expand=YES, fill=BOTH)

        self.cv.create_text(590, 460, text='v1.0', fill='black', font=('Times', 8, 'italic bold'))

        self.draw_picture()

    def make_preprocessorwin(self):
        new_win = Toplevel(self)
        PreprocessorWin(new_win).mainloop()

    def draw_picture(self):
        pass


if __name__ == '__main__':
    MainWindow().mainloop()