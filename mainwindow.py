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
    def __init__(self, parent=None):
        AbstractWindow.__init__(self, parent)
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

        self.prbtn = Button(fr, bg='#D3D3D3', text='Процессор', font=FONT, bd=8, relief=RAISED, state=DISABLED,
                            command=self.make_processorwin)

        self.prbtn.pack(expand=YES, fill=BOTH, pady=5)

        self.postprbtn = Button(fr, bg='#D3D3D3', text='Постпроцессор', font=FONT, bd=8, relief=RAISED, state=DISABLED,
                                command=self.make_postprocessorwin)
        self.postprbtn.pack(expand=YES, fill=BOTH)

        self.cv.create_text(590, 460, text='v1.0', fill='black', font=('Times', 8, 'italic bold'))

    def make_preprocessorwin(self):
        win = Toplevel(self)
        win.protocol('WM_DELETE_WINDOW', lambda win=win, self=self: self.make_active(win, 1))
        PreprocessorWin(win).mainloop()

    def make_active(self, win, type):
        win.destroy()
        if type == 1:
            self.prbtn['state'] = 'normal'
        else:
            self.postprbtn['state'] = 'normal'

    def make_processorwin(self):
        win = Toplevel(self)
        win.protocol('WM_DELETE_WINDOW', lambda win=win, self=self: self.make_active(win, 2))
        ProcessorWin(win).mainloop()

    def make_postprocessorwin(self):
        PostprocessorWin(Toplevel(self)).mainloop()

if __name__ == '__main__':
    root = Tk()
    MainWindow(root)
    root.mainloop()