import Locations
import Characters
import sqlite3


game_options = {}


def read_options(options_file: str):
    with open(options_file) as options:
        global game_options
        game_options = load(options)


if __name__ == '__main__':
    print('main')
