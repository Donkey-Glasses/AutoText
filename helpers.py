from random import choice

import sqlite3


class OptionList:
    def __init__(self):
        raise NotImplementedError


def connection_setup():
    connection = sqlite3.connect('..\\data\\game_data.dat')
    cursor = connection.cursor()
    return connection, cursor


def connection_cleanup(connection):
    connection.commit()
    connection.close()


def random_from_data(table: str, field: str, where_clause: str = None):
    con, cur = connection_setup()
    if where_clause is not None:
        cur.execute(f'SELECT {field} FROM {table} WHERE {where_clause}')
    else:
        cur.execute(f'SELECT {field} FROM {table}')
    return choice(cur.fetchall())[0]


def load_from_data_file(table: str, where_clause: str = None):

    con, cur = connection_setup()
    if where_clause is not None:
        query = f'SELECT * FROM {table} WHERE {where_clause}'
    else:
        query = f'SELECT * FROM {table}'
    cur.execute(query)
    data = cur.fetchall()
    connection_cleanup(con)
    return data[0]
