__author__ = 'dima'

from tkinter import *


class Drawbutton(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)

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
                      font=('Times', 14, 'italic bold')).pack(expand=YES, fill=BOTH)


