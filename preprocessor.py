__author__ = 'dima'

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
from rodstable import Rodstable
from nodestable import Nodestable
from construction import Construction
from savedata import save_data, get_data


class PreprocessorWin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(expand=YES, fill=BOTH)

        self.master.title('Окно препроцессора')
        self.make_widgets()

    def make_widgets(self):
        inner = Innerframe(self)
        inner.pack(side=BOTTOM)
        con = Construction(self)
        con.pack(side=TOP)
        PreprocessMenu(self.parent, inner, con)


class PreprocessMenu:
    def __init__(self, parent, inner_fr, con):
        self.menu_bar = Menu()
        self.parent = parent
        self.parent.config(menu=self.menu_bar)

        self.bottom_btns = inner_fr
        self.construction = con

        self.file_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)

        self.file_menu.add_command(label='Открыть', command=lambda self=self: self.bottom_btns.open_file())
        self.file_menu.add_command(label='Сохранить', command=lambda self=self: self.bottom_btns.save_file())
        self.file_menu.add_command(label='Назад к главному меню', command=lambda self=self: self.parent.destroy())
        self.file_menu.add_command(label='Выход', command=lambda self=self: self.parent.master.master.destroy())

        self.parameters = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Параметры', menu=self.parameters)

        self.rods_param = Menu(self.parameters)
        self.parameters.add_cascade(label='Стержни', menu=self.rods_param)

        self.nodes_param = Menu(self.parameters)
        self.parameters.add_cascade(label='Узлы', menu=self.nodes_param)

        self.rods_param.add_command(label='Отобразить лок. с-му координат', command=self.axes)

        self.rods_param.add_command(label='Пронумеровать стержни', command=self.rod_number)

        self.rods_param.add_command(label='Показать нагрузки', command=self.q_force)

        self.nodes_param.add_command(label='Пронумеровать узлы', command=self.node_number)

        self.nodes_param.add_command(label='Показать значение силы', command=self.force)

        self.parameters.add_command(label='Показать доп. параметры', command=self.show_other_param)
        self.parameters.add_command(label='Очистить всё', command=lambda self=self: self.construction.clear_all())

        self.help_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Помощь', menu=self.help_menu)

        self.help_menu.add_command(label='Справка', command=lambda self=self: self.bottom_btns.about())

    def show_other_param(self):
        if not self.construction.cv.gettags('other'):
            self.construction.draw_l_line()
            self.construction.draw_ea_line()
        else:
            self.construction.cv.delete('other')

    def axes(self):
        if not self.construction.cv.gettags('axes'):
            self.construction.draw_axes_system()
        else:
            self.construction.cv.delete('axes')

    def rod_number(self):
        if not self.construction.cv.gettags('rod_numb'):
            self.construction.draw_number_rod()
        else:
            self.construction.cv.delete('rod_numb')

    def q_force(self):
        if not self.construction.cv.gettags('q'):
            self.construction.draw_q_force()
        else:
            self.construction.cv.delete('q')

    def node_number(self):
        if not self.construction.cv.gettags('node_numb'):
            self.construction.draw_number_node()
        else:
            self.construction.cv.delete('node_numb')

    def force(self):
        if not self.construction.cv.gettags('force'):
            self.construction.draw_force()
        else:
            self.construction.cv.delete('force')


class Innerframe(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=640, height=120)
        self.pack(expand=YES, fill=BOTH)

        self.make_widgets()

    def make_widgets(self):
        self.opn_file_btn = Button(self, text='Открыть файл', font=('Times', 10, 'italic bold'),
                                command=self.open_file)
        self.opn_file_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.save_file_btn = Button(self, text='Сохранить в файл', font=('Times', 10, 'italic bold'),
                                    command=self.save_file)
        self.save_file_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.rodes_btn = Button(self, text='Параметры стержней', font=('Times', 10, 'italic bold'),
                               command=self.open_rods_win)
        self.rodes_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.nodes_btn = Button(self, text='Параметры узлов', font=('Times', 10, 'italic bold'),
                                command=self.open_nodes_win)
        self.nodes_btn.pack(side=LEFT, expand=YES, fill=BOTH)

        self.about_btn = Button(self, text='Справка', font=('Times', 10, 'italic bold'),
                                command=self.about)
        self.about_btn.pack(side=LEFT, expand=YES, fill=BOTH)

    def open_rods_win(self):
        Rodstable(Toplevel(self)).mainloop()

    def open_nodes_win(self):
        Nodestable(Toplevel(self)).mainloop()

    def open_file(self):
        filename = askopenfilename(parent=self, defaultextension='.db', filetypes=[('Database', '.db'),
                                                                                   ('SQLite3', '.sqlite3'),
                                                                                   ('SQLite', '.sqlite')],
                                   initialdir='/home/dima/Рабочий стол/САПР/Computer Mechanic/data')

        rods, nodes = get_data(filename)

        Rodstable.fill_dict(rods)
        Nodestable.set_dict(nodes)

    def save_file(self):
        filename = asksaveasfilename(parent=self, defaultextension='.db', filetypes=[('Database', '.db'),
                                                                                   ('SQLite3', '.sqlite3'),
                                                                                   ('SQLite', '.sqlite')],
                                   initialdir='/home/dima/Рабочий стол/САПР/Computer Mechanic/data')
        rods = Rodstable.get_data_about_rods()
        nodes = Nodestable.get_data_about_nodes()
        save_data(filename, rods, nodes)

    def about(self):
        win = Toplevel(self)
        Aboutwin(win).mainloop()


class Aboutwin(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=640, height=480)
        self.pack()
        self.master.title('Справка')

        self.make_widgets()

    def make_widgets(self):
        frame_btns = Frame(self)
        frame_btns.pack(side=LEFT, expand=YES, fill=BOTH)

        about_btn = Button(frame_btns, text='О программе', font=('Times', 12, 'italic bold'),
                           command=self.show_about_info)
        about_btn.pack(side=TOP, expand=YES, fill=BOTH)
        prepr_btn = Button(frame_btns, text='Препроцессор', font=('Times', 12, 'italic bold'),
                           command=self.show_prepr_info)
        prepr_btn.pack(side=TOP, expand=YES, fill=BOTH)
        pr_btn = Button(frame_btns, text='Процессор', font=('Times', 12, 'italic bold'),
                        command=self.show_pr_info)
        pr_btn.pack(side=TOP, expand=YES, fill=BOTH)
        postpr_btn = Button(frame_btns, text='Постпроцессор', font=('Times', 12, 'italic bold'),
                            command=self.show_postpr_info)
        postpr_btn.pack(side=TOP, expand=YES, fill=BOTH)

        self.frame_text = Frame(self)
        self.frame_text.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.text_widget = Text(self.frame_text)
        self.text_widget.pack(expand=YES, fill=BOTH)

    def show_about_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/about_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_prepr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/prepr_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_pr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/proc_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)

    def show_postpr_info(self):
        text = self.text_widget.get(1.0, END)
        if text:
            self.text_widget.delete(1.0, END)

        try:
            file_to_read = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/about/postproc_btns')
            text = file_to_read.readlines()

        except IOError as err:
            showerror('Ошибка', str(err))

        for item in text:
            self.text_widget.insert(END, item)



