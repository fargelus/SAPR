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

        prebtn = Preprocessorbutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        prebtn.pack(expand=YES, fill=BOTH)

        prbtn = Processorbutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        prbtn.pack(expand=YES, fill=BOTH, pady=5)

        postprbtn = Postprocessorbutton(fr, bg='#D3D3D3', bd=8, relief=RAISED)
        postprbtn.pack(expand=YES, fill=BOTH)

        self.draw_picture()

    def draw_picture(self):
        pass


if __name__ == '__main__':
    MainWindow().mainloop()