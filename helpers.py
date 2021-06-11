from random import choice, randint
from typing import List
from functools import partial
from datetime import datetime

import os
import sqlite3
import pickle


class Option:
    def __init__(self, text: str, selector: str, command, *args, **kwargs):
        self.text = text
        self.selector = selector
        self.command = partial(command, *args, **kwargs)

    def select(self):
        selection = self.command()
        return selection


class OptionList:
    def __init__(self, options: List[Option]):
        self.options = options

    def list_options(self):
        for option in self.options:
            print(f'{option.text}')

    def choose_option(self):
        print('You can do the following...')
        self.list_options()
        while True:
            selection = input(f'What do you want to do?  >> ')
            for item in self.options:
                if selection.lower().startswith(item.selector):
                    return item.select()

    @classmethod
    def rest_stop(cls):
        rest = Option('Rest', 'r', print, 'you have rested')  # TODO
        leave = Option('Leave', 'l', print, 'you walk out the door')  # TODO
        return OptionList([rest, leave])

    @classmethod
    def market(cls):
        buy = Option('Buy', 'b', print, 'What \'re ya buyin?')  # TODO
        sell = Option('Sell', 's', print, 'What are ya sellin?')  # TODO
        return OptionList([buy, sell])

    @classmethod
    def dungeon(cls):
        search = Option('Search', 's', print, 'You find no traps')  # TODO
        leave = Option('Leave', 'l', print, 'You run away!')  # TODO
        return OptionList([search, leave])


def connection_setup():
    user = os.getenv('HOMEPATH')
    dat = "\\PycharmProjects\\AutoText\\data\\game_data.dat"
    database = "c:\\" + user + dat
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    return connection, cursor


def connection_cleanup(connection):
    connection.commit()
    connection.close()


def random_from_data(table: str, field: str, where_clause: str = None, first_only: bool = True):
    con, cur = connection_setup()
    if where_clause is not None:
        cur.execute(f'SELECT {field} FROM {table} WHERE {where_clause}')
    else:
        cur.execute(f'SELECT {field} FROM {table}')
    response = cur.fetchall()
    connection_cleanup(con)
    if first_only:
        return choice(response)[0]
    else:
        return choice(response)


def random_from_data_weighted(table: str, field: str, where_clause: str = None):
    con, cur = connection_setup()
    if where_clause is not None:
        cur.execute(f'SELECT {field}, weight FROM {table} WHERE {where_clause}')
    else:
        cur.execute(f'SELECT {field}, weight FROM {table}')
    response = cur.fetchall()
    num_max = sum([item[-1] for item in response])
    num = randint(1, num_max)
    accumulate = 0
    for item in response:
        accumulate += item[-1]
        if accumulate >= num:
            return item[:-1]


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


def select_field_from_table(field: str, table: str, where_string: str = "") -> list:
    con, cur = connection_setup()
    try:
        query = f'SELECT {field} FROM {table} {where_string}'
        cur.execute(query)
    except sqlite3.OperationalError as oe:
        print(oe)
    data = cur.fetchall()
    connection_cleanup(con)
    for index, item in enumerate(data):
        data[index] = str(item[0])
    return data


def field_list_from_table(field_list: list, table: str, where_string: str = "") -> list:
    con, cur = connection_setup()
    data = []
    for item in field_list:
        cur.execute(f'SELECT {item} FROM {table} {where_string}')
        data.append(cur.fetchall()[0][0])
    connection_cleanup(con)
    return data


def save_blob(class_name: str, class_object):
    now = str(datetime.utcnow())
    save_id = "-".join([class_name, now])
    con, cur = connection_setup()
    class_binary = pickle.dumps(class_object)
    cur.execute("INSERT INTO save_objects VALUES (?, ?, ?)", (save_id, class_name, class_binary))
    con.commit()
    print('Saved!')
    return save_id


def load_blob(save_id: str):
    con, cur = connection_setup()
    cur.execute(f"SELECT blob FROM save_objects WHERE save_id='{save_id}'")
    con.commit()
    blob_objects = cur.fetchall()
    binary_list = [pickle.loads(item[0]) for item in blob_objects]
    return binary_list


if __name__ == "__main__":
    pass
