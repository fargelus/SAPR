__author__ = 'dima'

import sqlite3 as lite
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def read_result():
    con = lite.connect('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res.db')
    with con:
        cur = con.cursor()
        Nx = tuple(cur.execute('SELECT * FROM Nx'))
        Ux = tuple(cur.execute('SELECT * FROM Ux'))
        sigma = tuple(cur.execute('SELECT * FROM sigma'))
    return Nx, Ux, sigma


def write_result():
    Nx, Ux, sigma = read_result()
    doc = SimpleDocTemplate("/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res.pdf",
                            pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    Nx = get_writable_list(Nx)
    data = [['№', 'Значение'], Nx]
    print(data)

#     filename = open('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/toPdf.txt', 'w')
#     filename.write('\tNx\n\n')
#     write_table(filename, Nx)
#
#     filename.write('\n\n\n\tUx\n\n')
#     write_table(filename, Ux)
#
#     filename.write('\n\n\n\tSigma\n\n')
#     write_table(filename, sigma)
#
#     filename.close()
#
#     print(filename.name)
#     make_pdf(filename.name)
#
#


def get_writable_list(parameter):
    number_vals = [val[0] for val in parameter]
    vals = [val[1] for val in parameter]

    complex_list = []
    for item in zip(number_vals, vals):
        complex_list.append(list(item))

    print(complex_list)
    return complex_list


#
# def make_pdf(filename):
#     pdf_file = '/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res.pdf'
#     c = canvas.Canvas(pdf_file)
#
#     with open(filename) as file_to_write:
#         lines = file_to_write.readlines()
#         print(lines)
#
#     for line in lines:
#         c.drawString(100, 10, line)
#     c.save()


if __name__ == '__main__':
    write_result()
