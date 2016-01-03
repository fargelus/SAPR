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
    with con:
        data_rodes = tuple(cur.execute('SELECT * FROM Rods'))
        data_nodes = tuple(cur.execute('SELECT * FROM Nodes'))

    return data_rodes, data_nodes
