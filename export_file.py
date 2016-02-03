__author__ = 'dima'

import sqlite3 as lite
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def read_result(parameter):
    con = lite.connect('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res.db')
    with con:
        cur = con.cursor()
        Nx = tuple(cur.execute('SELECT * FROM Nx'))
        Ux = tuple(cur.execute('SELECT * FROM Ux'))
        sigma = tuple(cur.execute('SELECT * FROM sigma'))
    if str(parameter) == 'Nx':
        return Nx
    elif str(parameter) == 'Ux':
        return Ux
    elif str(parameter) == 'sigma':
        return sigma
    return


def write_result():
    make_pdf('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res_pdf/resNx.pdf', 'Nx')
    make_pdf('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res_pdf/resUx.pdf', 'Ux')
    make_pdf('/home/dima/Рабочий стол/САПР/Computer Mechanic/data/res_pdf/res_sigma.pdf', 'sigma')


def make_pdf(filename, parameter):
    parameter = read_result(parameter)
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    data = [['Number', 'Value']]
    write_data(parameter, data)

    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])

    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t = Table(data2)
    t.setStyle(style)

    elements.append(t)
    doc.build(elements)


def write_data(parameter, data):
    number_vals = [str(val[0]) for val in parameter]
    vals = [str(val[1]) for val in parameter]

    for item in zip(number_vals, vals):
        data.append(list(item))


if __name__ == '__main__':
    write_result()
