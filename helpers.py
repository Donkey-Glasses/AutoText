from random import choice

import sqlite3


class OptionList:
    def __init__(self):
        raise NotImplementedError


# def random_from_data(table: str, key):
#     with open(file_name) as f:
#         json_data = load(f)
#         return choice(json_data[key])


def load_from_data_file(table: str, where_clause: str = None):
    def setup():
        connection = sqlite3.connect('..\\data\\game_data.dat')
        cursor = connection.cursor()
        return connection, cursor

    def cleanup(connection):
        connection.commit()
        connection.close()

    con, cur = setup()
    if where_clause is not None:
        query = f'SELECT * FROM {table} WHERE {where_clause}'
    else:
        query = f'SELECT * FROM {table}'
    cur.execute(query)
    data = cur.fetchall()
    cleanup(con)
    return data[0]
