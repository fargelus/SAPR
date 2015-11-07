__author__ = 'dima'

from tkinter import *


class Processorbutton(Button):
    def __init__(self, parent=None, **options):
        Button.__init__(self, parent, options)
        self.config(text='Процессор', font=('Verdana', 14, 'italic bold'))

