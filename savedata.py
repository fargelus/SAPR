__author__ = 'dima'

import sqlite3 as lite
from os import getcwd


def save_rods(rods):
    initial_dir = getcwd()
    con = lite.connect(initial_dir + '/data/demo.db')
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS Rods')
    cur.execute('CREATE TABLE Rods(№ INTEGER, L INTEGER, A INTEGER, E INTEGER, σ INTEGER, q INTEGER);')
    for key in rods:
        cur.execute("INSERT INTO Rods(№, L, A, E, σ, q) VALUES(%s, %s, %s, %s, %s, %s)"
                    % (key, rods[key][0], rods[key][1], rods[key][2], rods[key][3], rods[key][4]))

    con.commit()


def save_nodes(nodes):
    initial_dir = getcwd()
    con = lite.connect(initial_dir + '/data/demo.db')
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS Nodes')
    cur.execute('CREATE TABLE Nodes(№ INTEGER, F INTEGER, Заделка Boolean);')
    for key in nodes:
        cur.execute("INSERT INTO Nodes(№, F, Заделка) VALUES(%s, %s, %s)"
                    % (key, nodes[key][0], nodes[key][1]))

    con.commit()


def save_data(filename, data_rodes, data_nodes):
    con = lite.connect(filename)
    cur = con.cursor()
    with con:
        cur.execute('DROP TABLE IF EXISTS Rods')
        cur.execute('CREATE TABLE Rods(№ INTEGER, L INTEGER, A INTEGER, E INTEGER, σ INTEGER, q INTEGER);')
        for key in data_rodes:
            cur.execute("INSERT INTO Rods(№, L, A, E, σ, q) VALUES(%s, %s, %s, %s, %s, %s)"
                    % (key, data_rodes[key][0], data_rodes[key][1], data_rodes[key][2],
                       data_rodes[key][3], data_rodes[key][4]))

        cur.execute('DROP TABLE IF EXISTS Nodes')
        cur.execute('CREATE TABLE Nodes(№ INTEGER, F INTEGER, Заделка Boolean);')
        for key in data_nodes:
            cur.execute("INSERT INTO Nodes(№, F, Заделка) VALUES(%s, %s, %s)"
                    % (key, data_nodes[key][0], data_nodes[key][1]))


def get_data(filename):
    con = lite.connect(filename)
    cur = con.cursor()
    data_rodes = ()
    data_nodes = ()
    with con:
        try:
            data_rodes = tuple(cur.execute('SELECT * FROM Rods'))
            data_nodes = tuple(cur.execute('SELECT * FROM Nodes'))
        except lite.OperationalError:
            pass

    return data_rodes, data_nodes


def save_res(Nx, Ux, sigma):
    initial_dir = getcwd()
    con = lite.connect(initial_dir + '/data/res.db')
    cur = con.cursor()
    with con:
        cur.execute('DROP TABLE IF EXISTS Rods')
        cur.execute('DROP TABLE IF EXISTS Nx')
        cur.execute('CREATE TABLE Nx(№ INTEGER, Val FLOAT);')

        cur.execute('DROP TABLE IF EXISTS Ux')
        cur.execute('CREATE TABLE Ux(№ INTEGER, Val FLOAT);')

        cur.execute('DROP TABLE IF EXISTS sigma')
        cur.execute('CREATE TABLE sigma(№ INTEGER, Val FLOAT);')

        for index, val in enumerate(Nx):
            cur.execute('INSERT INTO Nx(№, Val) VALUES (%s, %.2f)' % (index + 1, val))

        for index, val in enumerate(Ux):
            cur.execute('INSERT INTO Ux(№, Val) VALUES (%s, %.2f)' % (index + 1, val))

        for index, val in enumerate(sigma):
            cur.execute('INSERT INTO sigma(№, Val) VALUES (%s, %.2f)' % (index + 1, val))
